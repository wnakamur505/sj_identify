group_dict = {}
new_list = []

import math

with open("/home/ubuntu/environment/sj_identify/output_files/tsv_files/Binary_predictable_SNPs.tsv","r") as hin:

    for line in hin:
        f = line.rstrip('\n').split('\t')
        if f[0].startswith("Group"):continue
        group_no = f[0]
        snp_id =f[1]
        Others_Intercept = f[11]
        Others_X4 = f[12]
        Others_X5 = f[13]

        snp_info = [snp_id,Others_Intercept,Others_X4,Others_X5]
        
        group_dict[group_no] = snp_info
    
with open("/home/ubuntu/environment/GTEx_file/files/GTEx_SJ_count_and_genotype_binary.txt","r") as hin:

    for line in hin:
        f = line.rstrip('\n').split('\t')
        group_no = f[0] 
        GTEx_id = f[1]
        normal_SJ_count = f[2]
        abnormal_SJ_count = f[3]
        raw_genotype = f[4]
        
        if raw_genotype == "0/0": 
            str_genotype = "Homo_Ref"
            
        elif raw_genotype == "1/1": 
            str_genotype = "Others"
        
        else:
            str_genotype = "Others"

        if group_no in group_dict:
            snp_info = group_dict.get(group_no)
            
            snp_id = snp_info[0]
            Others_Intercept = snp_info[1]
            Others_X4 = snp_info[2]
            Others_X5 = snp_info[3]
     
            e = math.e
        
            l_Others = float(Others_Intercept) + float(Others_X4) * int(normal_SJ_count) + float(Others_X5)*int(abnormal_SJ_count)

            Others_p = math.exp(l_Others) / (1 + math.exp(l_Others))
            Homo_Ref_p = 1 / (1 + math.exp(l_Others))
            
            if Homo_Ref_p >- 0.5:
                prediction = "Homo_Ref"    
    
            if Others_p >= 0.5:
                prediction = "Others"

            if prediction == str_genotype:
                result = True
                
            else:
                result = False
                
            print(snp_id + "\t" + GTEx_id  + "\t" + normal_SJ_count + "\t" + abnormal_SJ_count + "\t" + raw_genotype + "\t" + str_genotype + "\t" + str(round(Homo_Ref_p, 3)) + "\t" + str(round(Others_p, 3)) + "\t" +  prediction + "\t" + str(result))