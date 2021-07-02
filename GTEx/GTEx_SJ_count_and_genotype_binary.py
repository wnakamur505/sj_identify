import os, glob, re

search_dict = {}

with open("/home/ubuntu/environment/GTEx_file/files/GTEx_group_GRCh37_binary.txt","r") as hin:
    for line in hin:
        f = line.rstrip('\n').split('\t')
        group_id = f[0]
        chr = f[1].replace("chr","")
        position = f[36]
        REF = f[32]
        ALT = f[33]
        GRCh37_snp_data = (chr,position,REF,ALT)
        if GRCh37_snp_data not in search_dict:
            search_dict[GRCh37_snp_data] = group_id

import ast
sample_id_list = []
pickup_dict = {}
with open("/home/ubuntu/environment/GTEx_file/files/GTEx_mini_haplogypecaller_binary.txt","r") as hin:
    for line in hin:
        F = line.rstrip('\n').split('\t')
        output = ast.literal_eval(F[0])
            
        if output[0].startswith("##"):continue
        target_snp = (output[0],output[1],output[3],output[4]) 

        if output[0].startswith("#"):
            for i in range(9,len(output)): 
                sample_id_list.append(output[i]) 

        if target_snp in search_dict: 
            group_id = search_dict[target_snp]
            for i in range(9,len(output)): 
                pickup_dict[(group_id,sample_id_list[i-9])] = output[i]


with open("/home/ubuntu/environment/GTEx_file/files/GTEx_counting_binary.txt","r") as hin: 

    for line in hin:
        f = line.rstrip('\n').split('\t')

        group_no = f[0]
        raw_sample_id = f[1]
        normal_SJ_count = f[2]
        abnormal_SJ_count = f[3]
        new_f = f[0] + "\t" + f[1] + "\t" + f[2] + "\t" + f[3]

        m = re.match("(GTEX-.*)-(0.*)",raw_sample_id)
        sample_id = m.group(1)

        search_position2 = (group_no,sample_id)
        
        GTEx_count = [f[1],f[2],f[3]]


        if search_position2 in pickup_dict:
            
            allele_status2 = pickup_dict[search_position2]
            m = re.match("(.\/.)(.*)",allele_status2)
            genotype =m.group(1)
            
            print(new_f + "\t" + genotype)