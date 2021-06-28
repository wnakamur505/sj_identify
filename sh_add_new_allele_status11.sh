#!/usr/bin/env bash

for i in $(seq 1 22)
do
    if [ ! -e /work/rawdata/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz ];then
        aws s3 cp s3://1000genomes/release/20130502/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz /work/rawdata/
        echo "DownLoaded chr ${i} vcf.gz file"
    fi
    
    if [ -e /work/rawdata/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz ];then
        echo "making chr"${i}"txt file"
        python3 add_new_allele_status11.py /work/rawdata/ALL.chr${i}.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz > add_new_allele_status11_chr${i}.txt
        
    fi
done

#[ -f /work/rawdata/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.tsv ] || gunzip /work/rawdata/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.tsv.gz
#echo "gunzip chrX_tsv.gz file :done"
#[ -f /work/rawdata/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.tsv ] && python3 add_new_allele_status10.py /work/rawdata/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.tsv > add_new_allele_status11_chrX.txt
#echo "making chrX_txt file :done"
#[ -f /work/rawdata/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.tsv ] && gzip /work/rawdata/ALL.chrX.phase3_shapeit2_mvncall_integrated_v1b.20130502.genotypes.tsv
#echo "gzip chrX_tsv file :done"


#[ -f /work/rawdata/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.tsv ] || gunzip /work/rawdata/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.tsv.gz
#echo "gunzip chrY_tsv.gz file :done"
#[ -f /work/rawdata/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.tsv ] && python3 add_new_allele_status10.py /work/rawdata/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.tsv > add_new_allele_status11_chrY.txt
#echo "making chrY_txt file :done"
#[ -f /work/rawdata/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.tsv ] && gzip /work/rawdata/ALL.chrY.phase3_integrated_v1b.20130502.genotypes.tsv
#echo "gzip chrY_tsv file :done"



#bash
#chmod +x sh_Untitled13.sh
#./sh_Untitled13.sh

