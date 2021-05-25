import os, glob
import re
#python3 countSJ9.py > countSJ9.txt


SJ_count_dict = {}
SJ2group_id_ref = {}
SJ2group_id_alt = {}
with open("grouping9.txt","r") as hin: 
    
#まず、辞書に見たい配列を入れる
        
    for line in hin:
        f = line.rstrip('\n').split('\t')
        group_id = f[0]
        Chr = f[1]
        Normal_SJ_start = str(int(f[2])+1)
        Normal_SJ_end = f[3]
        Abnormal_SJ_start = f[12]
        Abnormal_SJ_end = f[13]
        
        normal_SJ = (Chr,Normal_SJ_start,Normal_SJ_end)
        SJ2group_id_ref[normal_SJ] = group_id
        
        alt_SJ = (Chr, Abnormal_SJ_start, Abnormal_SJ_end)
        SJ2group_id_alt[alt_SJ] = group_id
        
        #print(SJ2group_id_alt)
        
with open("select_sample_considered_duplication.txt","r") as hin:
#with open("select_sample_considered_test.txt","r") as hin:
    
    for line in hin:
        f = line.rstrip('\n').split('\t')
        #print(f[0])
        ERR_id = f[0]
        #print(ERR_id)
        
        files = glob.glob(ERR_id + "/star/" + ERR_id + ".SJ.out.annot.tab")
        #print(files)
        for line in files:
            with open(line,"r") as hin:
                for line in hin:
                    F =line.rstrip('\n').split('\t')
                    #print(F)
                    if F[0].startswith('SJ_1') : continue
        
                    SJ_key = (F[0],F[1],F[2]) #SJ_keyは、ERR188021とかから、染色体・intronstart・intronendをとってきた。これが見たい辞書に入っているかを調べる。
                    #print(SJ_key)            
                    if SJ_key in SJ2group_id_ref: #SJ2group_id_refにSJ_key（見たい配列）があれば、
            
                        group_id = SJ2group_id_ref[SJ_key] #前格納した値（group_id） をgroup_idとして取得する。

                        SJ_count = F[6] #ただ変数を定義する。SJ_countはSTARの7列目。
                
                        if (group_id, ERR_id) not in SJ_count_dict:  #SJ_count_dictという最終的に集計したい辞書に、group_id,sample_idのkeyがなければ、
                            SJ_count_dict[(group_id, ERR_id)] = ["0", "0"] #valueをリスト["0","0"]にする。
                        SJ_count_dict[(group_id, ERR_id)][0] = SJ_count #valueの一つ目のリストに、SJ_countを入れる。
                
                
                    if SJ_key in SJ2group_id_alt:
            
                        group_id = SJ2group_id_alt[SJ_key]
               
                        SJ_count = F[6]  #左は変数、右は値. SJ_count =40(例)
                
                        if (group_id, ERR_id) not in SJ_count_dict:
                            SJ_count_dict[(group_id, ERR_id)] = ["0", "0"]
                        SJ_count_dict[(group_id, ERR_id)][1] = SJ_count # (=F[6])
            
                
for key in SJ_count_dict: #SJ_count_dictのkeyつまり(group_id,sample_id)を一つずつkeyという変数に入れる。上までの段階で、SJ_count_dictにkeyとvalueが入っている。

    counts = SJ_count_dict[key] #辞書に入ってたkeyをまた辞書で検索し、value(さっきリストにしたもの）が表示される。
    
    print_key = '\t'.join(key) #タプル(group_id,sample_id)をタブにして分解する。
    
    print(print_key + '\t' + counts[0] + '\t' + counts[1])
    
    #key ⇨ ('204', 'ERR188021')
    #counts ⇨ ['137', '0'] 
    #print_key → 204	ERR188021
    #print_key + '\t' + counts[0] + '\t' + counts[1] → 204	ERR188021	137	0