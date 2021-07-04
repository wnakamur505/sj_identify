#! /usr/bin/env bash

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