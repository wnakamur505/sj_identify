#####################################################
#make jitter images
#####################################################

library(tidyverse)
D <- read_tsv("GTEx_SJ_count_and_genotype.txt", col_names = FALSE)

D$mut <- rep("Homo Ref", nrow(D))
D$mut[D$X5 %in% c("0/1", "1/0")] <- "Het"
D$mut[D$X5 == "1/1"] <- "Homo Alt"
D$mut2 <- factor(D$mut, levels = c("Homo Ref", "Het", "Homo Alt"))

group_id_list <- sort(unique(D$X1))
#group_id_list <- c(3,5,11,30,65,83,88,89,94,100,123,126,164,179,213,227,239,249,259,283,286,307,355,409,421,436,438,477,502,516,607)
#group_id_list <- c(6,10,30,77,89,126,143,192,208,214,249,283,286,291,305,307,343,345,346,349,373,394,409,421,424,454,477,516,528,543,561,564,595,598,623)
#group_id_list <- c(387,209,215,379,252,171,89,65,286,404,193,30,531,424,181,397,415,246,564,348,310,287,264,519,495,349,309,53,10,126,470,66,480,439,553)


if (!dir.exists("/home/ubuntu/environment/sj_identify/GTEx/GTEximage")) {
  dir.create("/home/ubuntu/environment/sj_identify/GTEx/GTEximage")
}

for (i in group_id_list) {
  temp_D <-D %>% filter(X1 == i)
  ggplot(temp_D, aes(x = X3, y = X4, colour = mut2)) + 
    geom_jitter(height=0.2, width =0.2) + 
    theme_bw() +
    ggtitle(paste("group_id:", i)) +
    theme(legend.position = "bottom") +
    geom_smooth(mapping = aes(group = mut2,colour = mut2),method ="lm")+
    labs(title = temp_D$X1,x = "Normal SJ Counts", y ="Alternative SJ Counts", color = "Mutation Status") 
  ggsave(paste("/home/ubuntu/environment/sj_identify/GTEx/GTEximage/group_", i, ".pdf", sep = ""), width= 20, height = 20, unit = "cm")
}



