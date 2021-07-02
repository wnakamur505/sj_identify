library(tidyverse)

df_GTEx_binary <- read_tsv("/home/ubuntu/environment/GTEx_file/files/GTEx_judge_genotype_binary.txt", col_names = FALSE)

group_id_GTEx_binary <- sort(unique(df_GTEx_binary$X1))

res_GTEx_binary <- data.frame()

for (i in group_id_GTEx_binary ) {
  
  temp_df <- df_GTEx_binary %>% filter(X1 ==i)
  
  True_count <- sum (temp_df$X10 ==TRUE)
  
  FALSE_count <- sum (temp_df$X10 == FALSE)
  
  Accuracy <- True_count/ (True_count + FALSE_count)
  
  res_GTEx_binary  <- rbind(res_GTEx_binary,
                            data.frame(i,
                                       True_count,
                                       FALSE_count,
                                       True_count + FALSE_count,
                                       Accuracy %>% round(3)))
}
res_GTEx_binary

library(readr)
trgt_dir = "/home/ubuntu/environment/GTEx_file/files/"
path2csv = file.path(trgt_dir,"res_GTEx_binary.csv")
write_csv(res_GTEx_binary,path = path2csv)
#res_GTEx_binary_90<- res_GTEx_binary %>% filter(Accuracy.....round.3.>0.90)
