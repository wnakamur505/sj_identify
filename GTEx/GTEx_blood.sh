#! /usr/bin/env bash

#s3のマウントが必要（workのマウントは不要だけどやり方知りたい)

× aws s3 cp --recursive s3://wnakamur-tokyo/GTEx.rna.Blood.Wholo_Blood/ /home/ubuntu/environment/raw_data/GTEx.rna.Blood.Wholo_Blood/ --exclude="*" --include="*SJ.*.tab.gz"
◯ aws s3 cp --recursive s3://wnakamur-tokyo/GTEx.rna.Blood.Whole_Blood/ /home/ubuntu/environment/raw_data/GTEx.rna.Blood.Whole_Blood/ --exclude="*" --include="*.SJ.out.tab.gz"
#スペルミス

python3 GTEx_mini_haplotypecaller.py > GTEx_mini_haplotypecaller.txt
python3 GTEx_counting.py > GTEx_counting.txt
python3 GTEx_SJ_count_and_genotype.py > GTEx_SJ_count_and_genotype.txt
python3 GTEx_judge_genotype.py > GTEx_judge_genotype.txt

#! /usr/bin/env Rscript
Rscript GTEx_make_jitter.R
Rscript GTEx_calculate.R
Rscript GTEx_make_histogram.R

#bash
#chmod +x GTEx_blood.sh
#./GTEx_blood.sh

#last update：6/30