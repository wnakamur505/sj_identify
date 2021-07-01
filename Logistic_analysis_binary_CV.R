library(tidyverse)
library(caret)
library(readr)


df <- read_tsv("/home/ubuntu/environment/sj_identify/output_files/group_and_snp_info.txt", col_names = FALSE)
group_id <- sort(unique(df$X1))
snp_id <- sort(unique(df$X11))

set.seed(1985)
res_binary_cutmax5 <- data.frame()

df$genotype <- rep(NA,nrow(df))

df$genotype[df$X6 %in% c("0|0","0")] <-"Homo_Ref"
df$genotype[df$X6 %in% c("0|1", "1|0","1|1","1")] <-"Others"
df$genotype <- as.factor(df$genotype)

df$allele_count <- rep(NA,nrow(df))
df$allele_count [df$X6 %in% c("0|0","0")] <- 0
df$allele_count [df$X6 %in% c("0|1", "1|0")] <- 1
df$allele_count [df$X6 %in% c("1|1","1")] <-2

for (i in group_id) {
  
  temp_df <- df %>% filter(X1 ==i)
  
  temp_df_snp_id <- sort(unique(temp_df$X11))
  
  temp_df_genotype <- temp_df  %>% filter(genotype =="Others")
  max_Others <- max(temp_df_genotype$X5) 
  if (max_Others < 5) next
  
  
  if (sum(temp_df$genotype == "Others") ==0) next
  if (sum(temp_df$genotype == "Homo_Ref") == 0) next
    
  Homo_Ref_count <- sum(temp_df$allele_count==0)
  Hetero_count  <- sum(temp_df$allele_count==1)
  Homo_Alt_count<- sum(temp_df$allele_count==2)
  n =Homo_Ref_count + Hetero_count + Homo_Alt_count
  
  allele_freq= ((Homo_Ref_count * 0 +Hetero_count  * 1 +Homo_Alt_count* 2) / (nrow(temp_df) * 2) )
  q=1-allele_freq

  E_Homo_Alt_count_data = n*allele_freq^2
  E_Hetero_count_data = 2*n*allele_freq*q
  E_Homo_Ref_count_data = n*q^2
  
  chisq = (Homo_Ref_count - E_Homo_Ref_count_data)^2 / E_Homo_Ref_count_data + 
          (Hetero_count - E_Hetero_count_data)^2 / E_Hetero_count_data +
          (Homo_Alt_count - E_Homo_Alt_count_data)^2 / E_Homo_Alt_count_data
  
  index <-createDataPartition(temp_df$genotype, p=.8, list=FALSE, times=1)
  
  temp_df<- as.data.frame(temp_df)
  temp_df<- temp_df[, c(-1:-3,-6:-12,-14)] 
  
  train_df <- temp_df[index,]
  test_df <- temp_df[-index,]
  
  train_df$genotype <- as.factor(train_df$genotype)
  test_df$genotype <- as.factor(test_df$genotype)
  
  ctrlspecs <- trainControl(method="cv",number=5,
                            savePredictions = "all",
                            classProbs = TRUE)
  
  model <- train(genotype ~ X4 + X5,
                 data=train_df,
                 method ="glm",family=binomial,
                 trControl=ctrlspecs)
  
  coefficients_res = model$finalModel$coefficients
  Others_Intercept=coefficients_res[1]
  Others_X4=coefficients_res[2]
  Others_X5=coefficients_res[3]
  
  
  predictions <- predict(model, newdata=test_df)
  
  res_confusionMatrix <- confusionMatrix(data=predictions,test_df$genotype)
  
  Accuracy  <- res_confusionMatrix$overal[1]
  kappa <- res_confusionMatrix$overal[2]
  AccuracyLower <- res_confusionMatrix$overal[3]  
  AccuracyUpper <- res_confusionMatrix$overal[4]
  AccuracyNull <- res_confusionMatrix$overal[5]
  AccuracyPValue <- res_confusionMatrix$overal[6]
  McnemarPValue <- res_confusionMatrix$overal[7]
  
  df_binary <- data.frame(Accuracy,kappa,AccuracyLower,AccuracyUpper,AccuracyNull,AccuracyPValue,McnemarPValue)
  rownames(df_binary) <- c (i)
  
  res_binary_cutmax5 <- rbind(res_binary_cutmax5,
                      data.frame(Group_id = i,
                                temp_df_snp_id,
                                df_binary,
                                allele_freq,
                                chisq,
                                Others_Intercept,
                                Others_X4,
                                Others_X5))
}

result<- res_binary_cutmax5 %>% filter(Accuracy>0.95, allele_freq > 0.05,chisq <9.49)
trgt_dir = "/home/ubuntu/environment/sj_identify/output_files/csv_files"
path2csv = file.path(trgt_dir, "Binary_predictable_SNPs1.csv")
write_csv(result, path = path2csv)
#write_csv(res_binary_cutmax5, path = path2csv)