#!/usr/bin/env bash

#[ -f /work/rawdata/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.tsv ] || gunzip /work/rawdata/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.tsv.gz
#echo "gunzip tsv.gz file :done"
#[ -f /work/rawdata/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.tsv ] && python3 add_new_allele_status9.py /work/rawdata/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.tsv > add_new_allele_status9_chrX.txt
#echo "making txt file :done"
#[ -f /work/rawdata/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.tsv ] && gzip /work/rawdata/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.tsv
#echo "gzip tsv file :done"


#[ -f /work/rawdata/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.tsv ] || gunzip /work/rawdata/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.tsv.gz
#echo "gunzip tsv.gz file :done"
#[ -f /work/rawdata/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.tsv ] && python3 add_new_allele_status9.py /work/rawdata/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.tsv > add_new_allele_status9_chrY.txt
#echo "making txt file :done"
#[ -f /work/rawdata/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.tsv ] && gzip /work/rawdata/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.tsv
#echo "gzip tsv file :done"

#for i in $(seq 1 21)
#do
    #[ -f /work/rawdata/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.tsv ] || gunzip /work/rawdata/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.tsv.gz
    
    #echo "gunzip tsv.gz file :done"
    
    #[ -f /work/rawdata/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.tsv ] && python3 add_new_allele_status9.py /work/rawdata/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.tsv > add_new_allele_status9_chr${i}.txt
    
    #echo "making txt file :done"
    
    #[ -f /work/rawdata/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.tsv ] && gzip /work/rawdata/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.tsv
    
    #echo "gzip tsv file :done"
    
#done




#bash
#chmod +x sh_auto523.sh
#./sh_auto523.sh