library(tidyverse)

df_GTEx <- read_tsv("judge_GTEx_genotype.txt", col_names = FALSE)

group_id_GTEx <- sort(unique(df_GTEx2$X1))

res_GTEx <- data.frame()

for (i in group_id_GTEx) {
  
  temp_df <- df_GTEx %>% filter(X1 ==i)
  
  True_count <- sum (temp_df$X11 ==TRUE)
  
  FALSE_count <- sum (temp_df$X11 == FALSE)
  
  Accuracy <- True_count/ (True_count + FALSE_count)
  
  res_GTEx  <- rbind(res_GTEx,
                     data.frame(i,
                                True_count,
                                FALSE_count,
                                True_count + FALSE_count,
                                Accuracy %>% round(3)))
}
res_GTEx


library(readr)
trgt_dir = "/home/ubuntu/environment/sj_identify/GTEx"
path2csv = file.path(trgt_dir,"res_GTEx.csv")
write_csv(res_GTEx ,path = path2csv)
