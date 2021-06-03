#! /usr/bin/env bash
#chmod +x sh_all_run_063.sh
#./sh_all_run063.sh

python3 select_sample_considered_duplication.py > select_sample_considered_duplication.txt

selected_run_sample_list.py > selected_run_sample_list.txt

python3 extract_motif9.py > a9.bed

python3 vcftobed_all.py ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf >  GRCh37_ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.bed

/home/ubuntu/environment/current_issue/junc_utils/sen_genome/liftOver GRCh37_ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.bed hg19ToHg38.over.chain b.bed unmapped.bed

bedtools intersect -wo -a a9.bed -b b.bed > c9.bed

python3 fetch_motif_sequence.py hg38.fa > fetch_motif_sequence.txt #正常配列を取得

python3 reverse_complement9.py > reverse_complement9.txt #正常配列から相補鎖を取得

python3 search_motif9.py > search_motif9.txt　#モチーフの怪しいSNPの部分を同定

python3 screening_junction_DB_first_half.py wgEncodeGencodeBasicV37.txt > screening_junctionDB_first_half.txt

python3 screening_junction_DB_last_half.py screening_junctionDB_first_half.txt > screening_junctionDB.txt

python3 get_authentic_SJ_fromDB10.py > get_authentic_SJ_from_DB10.txt 

python3 grouping9.py > grouping10.txt 

python3 add_GRCh37_grouping9.py > add_GRCh37_grouping10.txt　

python3 countSJ_number.py > countSJ_number11.txt 

#python3 add_new_allele_status10.pyは、下のコマンドで。

chmod +x sh_auto523.sh
./sh_auto523.sh

python3 add_new_allele_status10_all.py > add_new_allele_status11_all.txt

python3 add_ERR_zero11.py > add_ERR_zero11.txt

python3 add_new_allele_status_all_zero10_included.py > add_new_allele_status_all_zero11_included.txt

#最終更新：6/2