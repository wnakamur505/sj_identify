import os, glob
import re
#python3 countSJ_number.py > countSJ_number10_1.txt
SJ_count_dict = {}
SJ2group_id_list_ref = {}
SJ2group_id_list_alt = {}

with open("grouping10.txt","r") as hin: 
#with open("test_kensyou61.txt","r") as hin:
    
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
        
        #normal_list = [normal_SJ,[group_id]]
        #alt_list =[alt_SJ,[group_id]]
        
        if normal_SJ not in SJ2group_id_list_ref: SJ2group_id_list_ref[normal_SJ] = []
        SJ2group_id_list_ref[normal_SJ].append(group_id)
        
        if alt_SJ not in SJ2group_id_list_alt: SJ2group_id_list_alt[alt_SJ] = []
        SJ2group_id_list_alt[alt_SJ].append(group_id)
            
    
    #print(SJ2group_id_list_alt)
    #{('chr3', '10318095', '10320610'): ['439', '440', '441', '442'], ('chr3', '10319173', '10320610'): ['342'], ('chr3', '10319317', '10320610'): ['193']}
    #print(SJ2group_id_list_ref)
    #{('chr3', '10318095', '10320870'): ['439'], ('chr3', '10318095', '10319138'): ['440'], ('chr3', '10318095', '10321049'): ['441'], ('chr3', '10318095', '10320508'): ['442'], ('chr3', '10319173', '10321049'): ['342'], ('chr3', '10319317', '10321049'): ['193']}
    
    #確認：ok

with open("select_sample_considered_duplication.txt","r") as hin:
    for line in hin:
        f = line.rstrip('\n').split('\t')
        ERR_id = f[0]
        files = glob.glob(ERR_id + "/star/" + ERR_id + ".SJ.out.annot.tab")
        for line in files:
            with open(line,"r") as hin:
                for line in hin:
                    F =line.rstrip('\n').split('\t')
                    
                    if F[0].startswith('SJ_1') : continue
                    
                    SJ_key = (F[0],F[1],F[2]) #SJ_keyは、ERR188021とかから、染色体・intronstart・intronendをとってきた。これが見たい辞書に入っているかを調べる。
                    #print(SJ_key) :('chr1', '46250120', '46257741')           
                    SJ_count = F[6] 
                    
                    
                    if SJ_key in SJ2group_id_list_ref: #SJ2group_id_refにSJ_key（見たい配列）があれば、
            
                        #if F[5] == "0": continue #(annotationついてない時はスルー)
                        #これがないと、248596⇨247850行になる。
                        group_id_list = SJ2group_id_list_ref[SJ_key] #前格納した値（group_id） をgroup_idとして取得する。
                        
                        for group_id in group_id_list:
                        
                            if (group_id, ERR_id) not in SJ_count_dict:  #SJ_count_dictという最終的に集計したい辞書に、group_id,sample_idのkeyがなければ、
                                SJ_count_dict[(group_id, ERR_id)] = ["0", "0"] #valueをリスト["0","0"]にする。
                            SJ_count_dict[(group_id, ERR_id)][0] = SJ_count #valueの一つ目のリスト：normal SJの数に、SJ_countを入れる。
                    
                    
                    if SJ_key in SJ2group_id_list_alt:
            
                        group_id_list = SJ2group_id_list_alt[SJ_key]
               
                        for group_id in group_id_list:
                        
                            if (group_id, ERR_id) not in SJ_count_dict:
                                SJ_count_dict[(group_id, ERR_id)] = ["0", "0"]
                            SJ_count_dict[(group_id, ERR_id)][1] = SJ_count # (=F[6])
                        
    #print(SJ_count_dict)
    #{('377', 'ERR188029'): ['14', '0'], ('207', 'ERR188029'): ['53', '0'],
                
                    """
                    for i in range (0,len(SJ2group_id_ref_list)):
                        
                        if SJ_key in SJ2group_id_ref_list[i]:
                            #print(SJ2group_id_ref_list)#:[[('chr2', '231513633', '231514081'), ['17']], 
                            group_id = SJ2group_id_ref_list[i][1][0]
                             #print(group2_id)
                            if (group_id, ERR_id) not in SJ_count_dict:
                            
                                SJ_count_dict[(group_id, ERR_id)]= ["0", "0"]
                            
                            SJ_count_dict[(group_id, ERR_id)][0] = SJ_count
                        
                    for i in range (0,len(SJ2group_id_alt_list)):
                        
                        if SJ_key in SJ2group_id_alt_list[i]:
                        
                            group_id = SJ2group_id_alt_list[i][1][0]        
                            
                            if (group_id, ERR_id) not in SJ_count_dict:
                        
                                SJ_count_dict[(group_id, ERR_id)]= ["0", "0"]
                            
                            SJ_count_dict[(group_id, ERR_id)][1] = SJ_count
                    """
                        
    #print(SJ_count_dict) #{('446', 'ERR188029'): ['1', '1'], ('377', 'ERR188029'): ['1', '1'],          
                        #group2_idでもgroup_idでも一緒('377', 'ERR188029'): ['14', '0'], ('207', 'ERR188029'): ['53', '0'],
                        
   
                
    
for key in SJ_count_dict: #SJ_count_dictのkeyつまり(group_id,sample_id)を一つずつkeyという変数に入れる。上までの段階で、SJ_count_dictにkeyとvalueが入っている。

    counts = SJ_count_dict[key] #辞書に入ってたkeyをまた辞書で検索し、value(さっきリストにしたもの）が表示される。
    
    print_key = '\t'.join(key) #タプル(group_id,sample_id)をタブにして分解する。
    
    print(print_key + '\t' + counts[0] + '\t' + counts[1])
    
    #key ⇨ ('204', 'ERR188021')
    #counts ⇨ ['137', '0'] 
    #print_key → 204	ERR188021
    #print_key + '\t' + counts[0] + '\t' + counts[1] → 204	ERR188021	137	0            