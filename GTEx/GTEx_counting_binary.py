import os, glob, re, gzip

SJ_count_dict = {}
SJ2group_id_list_ref = {}
SJ2group_id_list_alt = {}
group_id2_list =[]

with open("GTEx_group_GRCh37_binary.txt","r") as hin: 

    for line in hin:
        f = line.rstrip('\n').split('\t')
        group_id = f[0]
        Chr = f[1]
        Normal_SJ_start = str(int(f[2])+1)
        Normal_SJ_end = f[3]
        
        Abnormal_SJ_start = f[12]
        Abnormal_SJ_end = f[13]
        
        normal_SJ = (Chr,Normal_SJ_start,Normal_SJ_end)
        alt_SJ = (Chr, Abnormal_SJ_start, Abnormal_SJ_end)
        
        if normal_SJ not in SJ2group_id_list_ref: SJ2group_id_list_ref[normal_SJ] = []
        SJ2group_id_list_ref[normal_SJ].append(group_id)
        
        if alt_SJ not in SJ2group_id_list_alt: SJ2group_id_list_alt[alt_SJ] = []
        SJ2group_id_list_alt[alt_SJ].append(group_id)
            
        group_id2_list.append(group_id)

files = glob.glob("/home/ubuntu/environment/raw_data/GTEx.rna.Blood.Whole_Blood/GTEX-*.SJ.out.tab.gz")


for line in files:
    m = re.match("(.home.*\/)(GTEX.*)(.SJ.out.tab.gz)",line)

    GTEX_id = m.group(2)

    with gzip.open(line, mode='rt', encoding='utf-8') as hin:
        for line in hin:
            F =line.rstrip('\n').split('\t')
                    
            if F[0].startswith('SJ_1') : continue
                    
            SJ_key = (F[0],F[1],F[2]) 
    
            SJ_count = F[6] 
            for group2_id in group_id2_list:
                if (group2_id, GTEX_id) not in SJ_count_dict:
                    SJ_count_dict[(group2_id, GTEX_id)] = ["0", "0"] 
                    
                if SJ_key in SJ2group_id_list_ref: 
                    group_id_list = SJ2group_id_list_ref[SJ_key] 
                        
                    for group_id in group_id_list:
                        
                        if (group_id, GTEX_id) not in SJ_count_dict:  
                            SJ_count_dict[(group_id, GTEX_id)] = ["0", "0"] 
                        SJ_count_dict[(group_id, GTEX_id)][0] = SJ_count 
                        
                    
                if SJ_key in SJ2group_id_list_alt:
            
                    group_id_list = SJ2group_id_list_alt[SJ_key]
               
                    for group_id in group_id_list:
                        
                        if (group_id, GTEX_id) not in SJ_count_dict:
                            SJ_count_dict[(group_id, GTEX_id)] = ["0", "0"]
                        SJ_count_dict[(group_id, GTEX_id)][1] = SJ_count 
                        
    
for key in SJ_count_dict: 
    counts = SJ_count_dict[key] 
    print_key = '\t'.join(key) 
    print(print_key + '\t' + counts[0] + '\t' + counts[1])