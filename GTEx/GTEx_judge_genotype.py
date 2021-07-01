group_dict = {}
new_list = []

import math

with open("/home/ubuntu/environment/sj_identify/output_files/tsv_files/Multinominal_predictable_SNPs_ac90.tsv ","r") as hin:
#6	rs17464525	90.652	0.14331896551724138	2.855704211532184	0.122404	7.8560951450668375	-2.399668627763489	-0.27035864739778476	0.4485824036961372	2.7877235327504186	-0.30586118459985545	-4.873464778371911
    for line in hin:
        f = line.rstrip('\n').split('\t')
        #print(f)
        if f[0].startswith("Group"):continue
        group_no = f[0]
        snp_id =f[1]
        Homo_ALt_Intercept = f[7]
        Homo_ALt_X4 = f[8]
        Homo_ALt_X5 = f[9]
        Homo_Ref_Intercept = f[10]
        Homo_Ref_X4 = f[11]
        Homo_Ref_X5 = f[12]
        
        snp_info = [snp_id,Homo_ALt_Intercept,Homo_ALt_X4,Homo_ALt_X5,Homo_Ref_Intercept,Homo_Ref_X4,Homo_Ref_X5]
        
        group_dict[group_no] = snp_info
    
#with open("test0630.txt","r") as hin:
with open("GTEx_SJ_count_and_genotype.txt","r") as hin:

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
            str_genotype = "Homo_Alt"
        
        else:
            str_genotype = "Hetero"
        #print(raw_genotype)
        #print(str_genotype)
            
            
        if group_no in group_dict:
            snp_info = group_dict.get(group_no)
            
            snp_id = snp_info[0]
            Homo_ALt_Intercept = snp_info[1]
            Homo_ALt_X4 = snp_info[2]
            Homo_ALt_X5 = snp_info[3]
            Homo_Ref_Intercept = snp_info[4]
            Homo_Ref_X4 = snp_info[5]
            Homo_Ref_X5 = snp_info[6]
            
            e = math.e
        
            l_Alt = float(Homo_ALt_Intercept) + float(Homo_ALt_X4) * int(normal_SJ_count) + float(Homo_ALt_X5)*int(abnormal_SJ_count)
            l_Ref = float(Homo_Ref_Intercept) + float(Homo_Ref_X4) * int(normal_SJ_count) + float(Homo_Ref_X5)*int(abnormal_SJ_count)
        
            Homo_Alt_p = math.exp(l_Alt) / (1 + math.exp(l_Alt) + math.exp(l_Ref))
            Homo_Ref_p = math.exp(l_Ref) / (1 + math.exp(l_Alt) + math.exp(l_Ref))
            Hetero_p = 1 / (1 + math.exp(l_Alt) + math.exp(l_Ref))
            
            if Homo_Ref_p >- 0.5:
                prediction = "Homo_Ref"    
    
            if Homo_Alt_p >= 0.5:
                prediction = "Homo_Alt"
            
            if Hetero_p >= 0.5:
                prediction = "Hetero"
            
            if prediction == str_genotype:
                result = True
                
            else:
                result = False
                
            print(snp_id + "\t" + GTEx_id  + "\t" + normal_SJ_count + "\t" + abnormal_SJ_count + "\t" + raw_genotype + "\t" + str_genotype + "\t" + str(round(Homo_Ref_p, 3)) + "\t" + str(round(Hetero_p, 3)) + "\t" + str(round(Homo_Alt_p, 3)) + "\t" +  prediction + "\t" + str(result))