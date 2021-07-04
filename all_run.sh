#! /usr/bin/env bash

#aws s3 cp --recursive s3://wnakamur-tokyo/1000genomedata/ /home/ubuntu/environment/raw_data/ERRfiles/ --exclude="*" --include="ERR*/star/*.tab"

#for file in `ls /home/ubuntu/environment/raw_data/ERRfiles/ERR*/star/*.SJ.out.tab.gz`; 
#do gunzip $file; 
#done

#for file in `ls */star/*.SJ.out.tab`; 
#do bfile=${file%.SJ.out.tab}; 
#junc_utils annotate ${file} ${bfile}.SJ.out.annot.tab;
#done

# make a9.bed
python3 select_sample_considered_duplication.py > select_sample_considered_duplication.txt
echo "select_sample_considered_duplication.txt:done"
python3 selected_run_sample_list.py > selected_run_sample_list.txt
echo "selected_run_sample_list.txt:done"
python3 extract_motif9.py > a9.bed
echo "a9.bed:done"

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
echo "GRCh37_ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.bed:done"

#preintersect make b.bed
/home/ubuntu/environment/current_issue/junc_utils/sen_genome/liftOver GRCh37_ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.bed hg19ToHg38.over.chain b.bed unmapped.bed
echo "b.bed:done"

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
echo "c9.bed:done"

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

#it takes 4-5hours
python3 countSJ_number11.py > countSJ_number11.txt 
echo countSJ_number11.txt 

#it takes 4-5hours
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

python3 add_new_allele_status11_all.py > add_new_allele_status11_all.txt 
echo "add_new_allele_status11_all.txt:done"

python3 additional_SNP_information.py > additional_SNP_information.txt
echo "additional_SNP_information.txt:done"

python3 group_and_snp_info.py > group_and_snp_info.txt
echo "group_and_snp_info.txt:done"

#delete files
rm -f selected_run_sample_list.txt select_sample_considered_duplication.txt
rm -f ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf
rm -f GRCh37_ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.bed
rm -f a9.bed b.bed c9.bed unmapped.bed
rm -f fetch_motif_sequence.txt reverse_complement9.txt search_motif9.txt
rm -f screening_junctionDB_first_half.txt screening_junctionDB.txt
rm -f get_authentic_SJ_fromDB627.txt
rm -f grouping10.txt
rm -f countSJ_number11.txt
rm -f add_new_allele_status11_chr*.txt
rm -f additional_SNP_information.txt

#deletes tools
rm hg38.fa
rm wgEncodeGencodeBasicV37.txt
rm hg19ToHg38.over.chain
rm bedtools liftOver

#! /usr/bin/env Rscript
Rscript Logistic_result_multinom_CV.R 
#default：ac90,af5,cutoff4

Rscript Logistic_analysis_binary_CV.R
#default：ac90,af5,cutoff5

#last update：6/30

#chmod +x all_run.sh
#./all_run.sh