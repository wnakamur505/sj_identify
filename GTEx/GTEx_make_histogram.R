library(tidyverse)

df_GTEx <- read_tsv("judge_GTEx_genotype.txt", col_names = FALSE)

GTEx_id <- sort(unique(df_GTEx$X2))

df_GTEx_id_compare <- data.frame()

res_mismatch_all <- c()

for (i in GTEx_id) {
  
  temp_df_GTEx <- df_GTEx %>% filter(X2 ==i) %>% arrange(X1) 
    
  temp_df_GTEx <-temp_df_GTEx[, c(-3:-4,-7:-11)] 
  
  temp_df_GTEx $genotype <- rep(NA,nrow(temp_df_GTEx))
  temp_df_GTEx$genotype[temp_df_GTEx$X5 %in% c("0/0","0")] <-1
  temp_df_GTEx$genotype[temp_df_GTEx$X5 %in% c("0/1", "1|0")] <-2
  temp_df_GTEx$genotype[temp_df_GTEx$X5 %in% c("1/1","1")] <-3
  temp_df_GTEx$genotype <- as.numeric(temp_df_GTEx$genotype)
  
  GTEx_id_vec <-  c (temp_df_GTEx$genotype)
  df_GTEx_id_compare  <- rbind(df_GTEx_id_compare,
                               c(i,GTEx_id_vec))
}
#df_GTEx_id_compare
#これは、417行×20列のdataframe

names(df_GTEx_id_compare)[1] <- "GTEx_id"

comb1 <- combn(x=c(GTEx_id),m=2)
#これは、2行×86736列のdataframeだから、組み合わせは86736通り
#nrow(comb1)、#ncol(comb1)

data_number <- length(comb1)/2

for (j in (1:data_number)) {
  a <- comb1[1,j]
  b <- comb1[2,j]
  
  temp_a = df_GTEx_id_compare[df_GTEx_id_compare$GTEx_id==a,]
  temp_b = df_GTEx_id_compare[df_GTEx_id_compare$GTEx_id==b,]

  res_mismatch <- c(sum(as.integer(temp_a != temp_b)))
  
  res_mismatch_all <- c(res_mismatch_all,
                        res_mismatch)

}

res_mismatch_all

df_res_mismatch_all<-  data.frame(res_mismatch_all)

hist(res_mismatch_all) + 
ggsave(paste("/home/ubuntu/environment/sj_identify/GTEx/GTEximage/blood_histogram.pdf"), width= 20, height = 20, unit = "cm")
}

ggplot(df_res_mismatch_all) + 
  geom_density(aes(x=res_mismatch_all)) + 
  ggsave(paste("/home/ubuntu/environment/sj_identify/GTEx/GTEximage/blood_density_plot.pdf"), width= 20, height = 20, unit = "cm")
}
