#! /usr/bin/env bash
#chmod +x sh_all_run_524.sh
#./sh_all_run_524.sh

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

python3 get_authentic_SJ_from_junctionDB9.py > get_authentic_SJ_from_junctionDB9.txt #inputfile：screening_junctionDB.txt とsearch_motif3.txt
# exonDBであるscreening_junctionDB.txt とexon_searchするためにポジション修正したsearch_motif2.txtを重ねて、正常exonのポジションを取得。

python3 all_information_include_authentic_SJ9.py > all_information_include_authentic_SJ9.txt #inputfile：get_authentic_SJ_from_junctionDB3.txt
#どこにも引っ掛からなかったexonとかを除外して、データを扱いやすいようにアンパックしたりした。

python3 grouping9.py > grouping9.txt # input：all_information_include_authentic_SJ2.txt、output：grouping3.txt

#グループ名を1列目に取得。
python3 add_GRCh37_grouping9.py > add_GRCh37_grouping9.txt　#input:GRCh37_ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.bed、＆　grouping3.txt

python3 countSJ9.py > countSJ9.txt #(input:ERR*/star/ERR*.SJ.out.annot.tabと"grouping3.txt"、output:countSJ3.txt)
#取得した正常SJは、exonの座標だから、intron座標に戻す。正常SJの小さい番号の座標を+1する。
#groupidとsampleidと正常SJ数と異常SJ数を4列にした。

chmod +x sh_auto523.sh
./sh_auto523.sh

python3 add_new_allele_status9_all.py > add_new_allele_status9_all.txt

python3 add_ERR_zero_first_half.py > add_ERR_zero_first_half.txt

python3 add_ERR_zero_last_half.py > add_ERR_zero_last_half.txt