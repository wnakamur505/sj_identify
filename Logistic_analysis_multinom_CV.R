library(tidyverse)

df <- read_tsv("/home/ubuntu/environment/sj_identify/output_files/group_and_snp_info.txt", col_names = FALSE)
group_id <- sort(unique(df$X1))
#group_id <- c(6,10,30,65,89,126,192,208,214,251,285,286,291,308,345,346,376,394,410,421,453,477,528,543,595,623)

set.seed(1985)
res_ternary_cutoff2_logistic <- data.frame()

df$genotype <- rep(NA,nrow(df))
df$genotype[df$X6 %in% c("0|0","0")] <-"Homo_Ref"
df$genotype[df$X6 %in% c("0|1", "1|0")] <-"Het"
df$genotype[df$X6 %in% c("1|1","1")] <-"Homo_Alt"
df$genotype <- as.factor(df$genotype)


df$allele_count <- rep(NA,nrow(df))
df$allele_count [df$X6 %in% c("0|0","0")] <- 0
df$allele_count [df$X6 %in% c("0|1", "1|0")] <- 1
df$allele_count [df$X6 %in% c("1|1","1")] <-2

for (i in group_id) {
  
  temp_df <- df %>% filter(X1 ==i)
  
  temp_df_snp_id <- sort(unique(temp_df$X11))
  
  temp_df_genotype <- temp_df  %>% filter(genotype =="Homo_Alt")
  
  if (sum(temp_df$genotype == "Homo_Alt") ==0) next
  
  max_Homo_Alt <- max(temp_df_genotype$X5) 
  
  if (max_Homo_Alt < 4) next
  
  Homo_Ref_count <- sum(temp_df$allele_count==0)
  Hetero_count  <- sum(temp_df$allele_count==1)
  Homo_Alt_count<- sum(temp_df$allele_count==2)
  n =Homo_Ref_count + Hetero_count + Homo_Alt_count
  
  allele_freq_obs_data= ((Homo_Ref_count * 0 +Hetero_count  * 1 +Homo_Alt_count* 2) / (nrow(temp_df) * 2) )
  q_obs_data =1-allele_freq_obs_data
  
  E_Homo_Alt_count_data = n*allele_freq_obs_data^2
  E_Hetero_count_data = 2*n*allele_freq_obs_data*q_obs_data
  E_Homo_Ref_count_data = n*q_obs_data^2
  
  chisq_obs_data = (Homo_Ref_count - E_Homo_Ref_count_data)^2 / E_Homo_Ref_count_data + 
    (Hetero_count - E_Hetero_count_data)^2 / E_Hetero_count_data +
    (Homo_Alt_count - E_Homo_Alt_count_data)^2 / E_Homo_Alt_count_data
  
  #allele_freq_open_data　<- as.numeric(temp_df[1,12])
  
  #q_open_data =1-allele_freq_open_data
  
  #E_Homo_Alt_count_open_data = n*allele_freq_open_data^2
  #E_Hetero_count_open_data = 2*n*allele_freq_open_data*q_open_data
  #E_Homo_Ref_count_open_data = n*q_open_data^2
  
  #chisq_open_data = (Homo_Ref_count - E_Homo_Ref_count_open_data)^2 / E_Homo_Ref_count_open_data + 
    #(Hetero_count - E_Hetero_count_open_data)^2 / E_Hetero_count_open_data +
    #(Homo_Alt_count - E_Homo_Alt_count_open_data)^2 / E_Homo_Alt_count_open_data
  
  temp_df<- temp_df[, c(-1:-3,-6:-12,-14)] 
  temp_df<- as.data.frame(temp_df)
  
  if (sum(temp_df$genotype == "Het") == 0) {
    next
  }
  if (sum(temp_df$genotype == "Homo_Ref") == 0) {
    next
  }
  if (sum(temp_df$genotype == "Homo_Alt") == 0) {
    next
  }
  
  library(caret)
  
  Accuracy_vec <- vector()
  
  for (j in 1:5){
    
    index <-createDataPartition(temp_df$genotype, p=.8, list=FALSE, times=1)
    
    train_df <- temp_df[index,]
    test_df <- temp_df[-index,]
    
    train_df$genotype <- relevel(train_df$genotype, ref = "Het")
    
    require(nnet)
    
    multinom_model <- multinom(genotype ~ ., data = temp_df)
    
    summary(multinom_model)
    
    train_df$ClassPredicted <- predict(multinom_model, newdata = train_df, "class")
    test_df$ClassPredicted <- predict(multinom_model, newdata = test_df, "class")
    tab <- table(test_df$genotype, test_df$ClassPredicted)
    Accuracy<- round((sum(diag(tab))/sum(tab))*100,2)
    
    Accuracy_vec <- c(Accuracy_vec,Accuracy)
    
    coefficients_res = multinom_model %>% coefficients()
    
  }
  
  Accuracy_Avg<- mean(Accuracy_vec)

  Homo_ALt_Intercept=coefficients_res[1,1]
  Homo_ALt_X4=coefficients_res[1,2]
  Homo_ALt_X5=coefficients_res[1,3]
  Homo_Ref_Intercept=coefficients_res[2,1]
  Homo_Ref_X4=coefficients_res[2,2]
  Homo_Ref_X5=coefficients_res[2,3]
  
  res_ternary_cutoff2_logistic <- rbind(res_ternary_cutoff2_logistic,
                               data.frame(Group_id = i,
                                          temp_df_snp_id,
                                          Accuracy_Avg,
                                          allele_freq_obs_data,
                                          chisq_obs_data,
                                          #allele_freq_open_data,
                                          #chisq_open_data,
                                          Homo_ALt_Intercept,
                                          Homo_ALt_X4,
                                          Homo_ALt_X5,
                                          Homo_Ref_Intercept,
                                          Homo_Ref_X4,
                                          Homo_Ref_X5))
}

result <- res_ternary_cutoff2_logistic %>% filter(Accuracy_Avg>90,allele_freq_obs_data > 0.05,chisq_obs_data<9.49)

library(readr)
trgt_dir = "/home/ubuntu/environment/sj_identify/output_files/files"
path2csv = file.path(trgt_dir, "Multinominal_predictable_SNPs1.csv")
write_csv(result, path = path2csv)
#write_csv(res_ternary_cutoff2_logistic, path = path2csv)

"""
if (!dir.exists("/home/ubuntu/environment/sj_identify/made_files/jitter_image")) {
  dir.create("/home/ubuntu/environment/sj_identify/made_files/jitter_image")
}

for (i in group_id) {
  temp_df <-df %>% filter(X1 == i)
  ggplot(temp_df, aes(x = X4, y = X5, colour = genotype)) + 
    geom_jitter(height=0.2, width =0.2) + 
    theme_bw() +
    ggtitle(paste("group_id:", i)) +
    theme(legend.position = "bottom") +
    geom_smooth(mapping = aes(group = genotype,colour = genotype),method ="lm")+
    labs(title = temp_df$X11,x = "Normal SJ Counts", y ="Alternative SJ Counts", color = "Mutation Status") 
  ggsave(paste("/home/ubuntu/environment/sj_identify/made_files/jitter_image/group_", i, ".pdf", sep = ""), width= 20, height = 20, unit = "cm")
}
"""