import csv
import sys
import gzip
import re
res = []

search_dict={}
with open("GTEx_group_GRCh37.txt","r") as hin:
    for line in hin:
        f = line.rstrip('\n').split('\t')
        group_id = f[0]
        chr = f[1].replace("chr","")
        GRCh37_position =f[36]
        REF = f[3]
        ALT = f[4]
        snp_data = (chr,GRCh37_position,REF,ALT)
        
        if group_id not in search_dict: search_dict[group_id] = []
        search_dict[group_id].append(snp_data)
    
with gzip.open("/home/ubuntu/environment/s3/GTEx_WholeGenomeSeq/GTEx_Analysis_2016-01-15_v7_WholeGenomeSeq_652Ind_GATK_HaplotypeCaller.vcf.gz", mode='rt', encoding='utf-8') as hin:
    for line in hin:
        
        f = line.rstrip('\n').split('\t')
        if f[0].startswith("#"):
            print(f)
        elif f[0].startswith("##"):
            print(f)
        else:

            chr = f[0]
            position = f[1]
            REF =f[3]
            ALT =f[4]

            snp_data = (chr,position,REF,ALT)
            

            for key in search_dict:
                if snp_data == search_dict.get(key)[0]:
                    print(f)