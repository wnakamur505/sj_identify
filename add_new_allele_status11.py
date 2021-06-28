import csv
import sys
import gzip

search_list=[]
search_dict={}
with open("add_GRCh37_grouping10.txt","r") as hin: 
    for line in hin:
        f = line.rstrip('\n').split('\t')
        group_id = f[0]
        chr = f[1].replace("chr","")
        REF = f[32]
        ALT = f[33]
        ver37_position = f[36] 
        snp_data = (chr,ver37_position,REF,ALT)
        snp_list = [snp_data,[group_id]]
        
        if snp_data not in search_dict:
            search_dict[snp_data] = group_id
        
        elif snp_data in search_dict:
            search_list.append(snp_list)

pickup_dict ={}
sample_id_list = [] 
input_file = sys.argv[1]
with gzip.open(input_file, mode='rt', encoding='utf-8') as hin:

    for line in hin:
        F = line.rstrip('\n').split('\t')
        if F[0].startswith("##"):continue
        if F[0].startswith("#"): 
            for i in range(9,len(F)): 
                sample_id_list.append(F[i]) 
        target_snp = (F[0],F[1],F[3],F[4]) 
        if target_snp in search_dict: 
            group_id = search_dict[target_snp]
            for i in range(9,len(F)): 
                pickup_dict[(group_id,sample_id_list[i-9])] = F[i]
            
        for i in range (0,len(search_list)):
            if target_snp in search_list[i]:
                group_id = search_list[i][1][0]

                for i in range(0,len(F)-9):
                    pickup_dict[(group_id,sample_id_list[i])] = F[i+9]
conversion_dict={}

with open ("SraRunTable.txt","r") as hin:
    for line in hin:
        f = line.rstrip('\n').split('\t')
        if f[0].startswith("Run"):continue
        err_id =f[0]
        hg_id = f[1].replace("GEUV:","")
        conversion_dict[err_id] = hg_id

with open ("countSJ_number11.txt","r") as hin:

    for line in hin:
        f = line.rstrip('\n').split('\t')
        err_id2 = f[1]
        if err_id2 in conversion_dict:
            hg_id2 = conversion_dict.get(f[1]) 
            new_f = f[0] + "\t" + hg_id2 + "\t" + f[1] + "\t" + f[2] + "\t" + f[3]
           
            search_position2 = (f[0],hg_id2)
            
            
            if search_position2 in pickup_dict:
            
                allele_status2 = pickup_dict[search_position2]
                
                print(new_f + "\t" + allele_status2)
                
                #python3 Untitled13.py /work/rawdata/ALL.chr22.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz