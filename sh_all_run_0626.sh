#! /usr/bin/env bash


# collecting ERR samples

#NOTE VIRVINIA!
#aws s3 cp --recursive s3://sra-virginia/analysis/ERR*/ ./  --exclude="*" --include="*SJ.out.tab.gz"

for file in `ls */star/*.SJ.out.tab.gz`; 
do gunzip $file; 
done

for file in `ls */star/*.SJ.out.tab`; 
do bfile=${file%.SJ.out.tab}; 
junc_utils annotate ${file} ${bfile}.SJ.out.annot.tab;
done

# make a9.bed
python3 select_sample_considered_duplication.py > select_sample_considered_duplication.txt

python3 selected_run_sample_list.py > selected_run_sample_list.txt

python3 extract_motif9.py > a9.bed

#ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf.gz DL
if [ -e ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf ];then
        echo "ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf:exist"

elif [ -e ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf.gz ]; then
        echo "gunzip ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf.gz"
        gunzip ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf.gz
else
    aws s3 cp s3://1000genomes/release/20130502/ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf.gz ./
    echo "gunzip ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf.gz"
    gunzip ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf.gz
fi


#liftOver DL
if [ ! -e liftOver ]; then
    wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/liftOver
    chmod +x liftOver
    echo "chmod +x liftOver:done"
else
    chmod +x liftOver
    echo "chmod +x liftOver:done"
fi


#hg19ToHg38.over.chain.gz DL
if [ -e hg19ToHg38.over.chain ];then
    echo "hg19ToHg38.over.chain:exist"
elif [ -e hg19ToHg38.over.chain.gz ]; then
    echo "gunzip hg19ToHg38.over.chain.gz"
    gunzip hg19ToHg38.over.chain.gz
else
    wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/liftOver/hg19ToHg38.over.chain.gz
    echo "gunzip hg19ToHg38.over.chain.gz"
    gunzip hg19ToHg38.over.chain.gz
fi

#make bed file
python3 vcftobed_all.py ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf >  GRCh37_ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.bed

#preintersect make b.bed
/home/ubuntu/environment/current_issue/junc_utils/sen_genome/liftOver GRCh37_ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.bed hg19ToHg38.over.chain b.bed unmapped.bed

#bedtools DL
if [ ! -e bedtools ]; then
    wget https://github.com/arq5x/bedtools2/releases/download/v2.30.0/bedtools.static.binary
    mv bedtools.static.binary bedtools
    chmod a+x bedtools
    echo "chmod a+x bedtools:done"
else
    chmod a+x bedtools
    echo "chmod a+x bedtools:done"
fi

# bedtools intersect
bedtools intersect -wo -a a9.bed -b b.bed > c9.bed

############ここまでやってみる########## Ok 

#hg38.fa.gz DL
if [ -e hg38.fa ];then
    echo "hg38.fa:exist"
elif [ -e hg38.fa.gz ]; then
    echo "gunzip hg38.fa.gz"
    gunzip hg38.fa.gz
else
    wget https://hgdownload.cse.ucsc.edu/goldenpath/hg38/bigZips/hg38.fa.gz
    echo "gunzip hg38.fa.gz"
    gunzip hg38.fa.gz
fi


python3 fetch_motif_sequence.py hg38.fa > fetch_motif_sequence.txt 
echo fetch_motif_sequence.txt

python3 reverse_complement9.py > reverse_complement9.txt 
echo reverse_complement9.txt

python3 search_motif9.py > search_motif9.txt 
echo search_motif9.txt

#wgEncodeGencodeBasicV37.txt.gz DL
if [ -e wgEncodeGencodeBasicV37.txt ];then
        echo "wgEncodeGencodeBasicV37.txt:exist"
elif [ -e wgEncodeGencodeBasicV37.txt.gz ]; then
        echo "gunzip wgEncodeGencodeBasicV37.txt.gz"
        gunzip wgEncodeGencodeBasicV37.txt.gz
else
    wget http://hgdownload.cse.ucsc.edu/goldenpath/hg38/database/wgEncodeGencodeBasicV37.txt.gz
    echo "gunzip wgEncodeGencodeBasicV37.txt.gz"
    gunzip wgEncodeGencodeBasicV37.txt.gz
fi


python3 screening_junction_DB_first_half.py wgEncodeGencodeBasicV37.txt > screening_junctionDB_first_half.txt
echo screening_junctionDB_first_half.txt

python3 screening_junction_DB_last_half.py screening_junctionDB_first_half.txt > screening_junctionDB.txt
echo screening_junctionDB.txt

python3 get_authentic_SJ_fromDB627.py > get_authentic_SJ_fromDB627.txt
echo get_authentic_SJ_from_DB627.txt 

python3 grouping10.py > grouping10.txt 
echo grouping10.txt 

python3 add_GRCh37_grouping9.py > add_GRCh37_grouping10.txt　
echo add_GRCh37_grouping10.txt

python3 countSJ_number.py > countSJ_number11.txt いまここ出待ち。
echo countSJ_number11.txt 


#python3 add_new_allele_status11.py is below
chmod +x sh_add_new_allele_status11.sh
./sh_add_new_allele_status11.sh

##########ここまで動作確認済み############

python3 add_new_allele_status11_all.py > add_new_allele_status11_all.txt

python3 add_ERR_zero11.py > add_ERR_zero11.txt　これ多分いらない。

python3 add_new_allele_status_all_zero10_included.py > add_new_allele_status_all_zero11_included.txt これ多分いらない。

python3 additional_SNP_information.py > additional_SNP_information.txt

python3 group_and_snp_info.py > group_and_snp_info.txt

#! /usr/bin/env Rscript

#make accuracy of specific 26snps
Rscript Logistic_result_multinom_CV.R #output:ac90_af5_HEW5_res_ternary_cutoff2_logistic.txt

#最終更新：6/26

#chmod +x sh_all_run_0626.sh
#./sh_all_run0626.sh
