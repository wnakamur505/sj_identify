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
    #print(SJ2group_id_list_alt)
    #{('chr1', '113900401', '113901278'): ['6'], ('chr2', '54106342', '54135452'): ['10'], ('chr4', '107670864', '107682014'): ['30'], ('chr7', '150435160', '150442548'): ['65'], ('chr11', '57426317', '57426587'): ['89'], ('chr14', '73787506', '73789026'): ['126'], ('chr2', '118103855', '118107089'): ['192'], ('chr6', '31356886', '31357085'): ['208'], ('chr6', '157322806', '157323001'): ['214'], ('chr16', '1312559', '1314019'): ['251'], ('chr22', '45171153', '45171599'): ['285'], ('chr1', '1228947', '1231506'): ['286'], ('chr1', '54723730', '54728345'): ['291'], ('chr6', '166948626', '166952083'): ['308'], ('chr4', '48228660', '48264379'): ['345', '346'], ('chr20', '35632924', '35664358'): ['376'], ('chr9', '15468119', '15468629'): ['394'], ('chr17', '81512361', '81512600'): ['410'], ('chr2', '27132924', '27133125'): ['421'], ('chr12', '126730804', '126732363'): ['453'], ('chr18', '36780189', '36781798'): ['477'], ('chr1', '205623892', '205627741'): ['528'], ('chr20', '35659015', '35664358'): ['543'], ('chr15', '99729732', '99731554'): ['595'], ('chr14', '50532159', '50532461'): ['623']}
    #print(SJ2group_id_list_ref)
    #{('chr1', '113900401', '113904604'): ['6'], ('chr2', '54057361', '54135452'): ['10'], ('chr4', '107660073', '107682014'): ['30'], ('chr7', '150433830', '150442548'): ['65'], ('chr11', '57426353', '57426587'): ['89'], ('chr14', '73787510', '73789026'): ['126'], ('chr2', '118106904', '118107089'): ['192'], ('chr6', '31356958', '31357085'): ['208'], ('chr6', '157322806', '157323411'): ['214'], ('chr16', '1312604', '1314019'): ['251'], ('chr22', '45171178', '45171599'): ['285'], ('chr1', '1228947', '1231891'): ['286'], ('chr1', '54722800', '54728345'): ['291'], ('chr6', '166948626', '166952487'): ['308'], ('chr4', '48228660', '48269751'): ['345', '346'], ('chr20', '35632924', '35664801'): ['376'], ('chr9', '15466860', '15468629'): ['394'], ('chr17', '81512361', '81512614'): ['410'], ('chr2', '27132924', '27133116'): ['421'], ('chr12', '126730804', '126732342'): ['453'], ('chr18', '36780189', '36798448'): ['477'], ('chr1', '205623892', '205631631'): ['528'], ('chr20', '35659015', '35664759'): ['543'], ('chr15', '99729732', '99733344'): ['595'], ('chr14', '50532159', '50532399'): ['623']}
    

files = glob.glob("/home/ubuntu/environment/raw_data/GTEx.rna.Blood.Whole_Blood/GTEX-*.SJ.out.tab.gz")
#simpleで良い
#files = glob.glob("/work/GTEx.rna.Blood.Whole_Blood/GTEX-*.SJ.out.annot.tab")
#files = glob.glob("/work/GTEx.rna.Muscle.Muscle-Skeletal/GTEX-*.SJ.out.annot.tab")
#print(files)

for line in files:
    #print(line)
#file = glob.glob("/work/GTEx.rna.Blood.Whole_Blood/GTEX-111YS-0006-SM-5NQBE.SJ.out.annot.tab")
#for line in file:
    m = re.match("(.home.*\/)(GTEX.*)(.SJ.out.tab.gz)",line)
    #m = re.match("(/home/ubuntu/environment/raw_data/GTEx.rna.Blood.Whole_Blood/)(GTEX-*)(.SJ.out.tab.gz)",line)
    #m = re.match("(/work/GTEx.rna.Muscle.Muscle-Skeletal/)(GTEX.*)(.SJ.out.annot.tab)",line) #(GTEX.*)(\.SJ.out.tab.gz)
    
    GTEX_id = m.group(2)
    #print(GTEX_id)
    
    with gzip.open(line, mode='rt', encoding='utf-8') as hin:
        for line in hin:
            F =line.rstrip('\n').split('\t')
                    
            if F[0].startswith('SJ_1') : continue
                    
            SJ_key = (F[0],F[1],F[2]) 
                #print(SJ_key) :(chr1    14830   15020)  
                    #chr1    14830   15020   2       2       0       1       0       18      Alternative 5'SS        ---     WASH7P(NR_024540)       10      s       0       WASH7P(NR_024540)       9       *       *

            SJ_count = F[6] 
                    # 1
            for group2_id in group_id2_list:
                if (group2_id, GTEX_id) not in SJ_count_dict:
                    SJ_count_dict[(group2_id, GTEX_id)] = ["0", "0"] 
                    
                if SJ_key in SJ2group_id_list_ref: 
                        #if F[5] == "0": continue #(annotationついてない時はスルー)
                        #これがないと、248596⇨247850行になる。
                    group_id_list = SJ2group_id_list_ref[SJ_key] #前格納した値（group_id） をgroup_idとして取得する。
                        
                    for group_id in group_id_list:
                        
                        if (group_id, GTEX_id) not in SJ_count_dict:  #SJ_count_dictという最終的に集計したい辞書に、group_id,sample_idのkeyがなければ、
                            SJ_count_dict[(group_id, GTEX_id)] = ["0", "0"] #valueをリスト["0","0"]にする。
                    #SJ_count_dict[(group_id, GTEX_id)][0] = SJ_count #valueの一つ目のリスト：normal SJの数に、SJ_countを入れる。
                        SJ_count_dict[(group_id, GTEX_id)][0] = SJ_count #valueの一つ目のリスト：normal SJの数に、SJ_countを入れる。
                    
                    
                if SJ_key in SJ2group_id_list_alt:
            
                    group_id_list = SJ2group_id_list_alt[SJ_key]
               
                    for group_id in group_id_list:
                        
                        if (group_id, GTEX_id) not in SJ_count_dict:
                            SJ_count_dict[(group_id, GTEX_id)] = ["0", "0"]
                        SJ_count_dict[(group_id, GTEX_id)][1] = SJ_count # (=F[6])
                        
    #print(SJ_count_dict)
    #{('377', 'ERR188029'): ['14', '0'], ('207', 'ERR188029'): ['53', '0'],

    
for key in SJ_count_dict: 
    counts = SJ_count_dict[key] 
    print_key = '\t'.join(key) 
    print(print_key + '\t' + counts[0] + '\t' + counts[1])
    
    #key ⇨ ('204', 'ERR188021')
    #counts ⇨ ['137', '0'] 
    #print_key → 204	ERR188021
    #print_key + '\t' + counts[0] + '\t' + counts[1] → 204	ERR188021	137	0            