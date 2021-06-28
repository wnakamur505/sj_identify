from collections import defaultdict
start2junc_dict = {}
end2junc_dict = {}
start2junc_list =[]
end2junc_list = []

with open ("screening_junctionDB.txt",'r') as hin:
    for line in hin:
        f = line.rstrip('\n').split('\t')
        start_posi = (f[0],f[1]) 
        end_posi = (f[0],f[2]) 
        SJ_posi = (f[0],f[1],f[2]) 
        
        if start_posi not in start2junc_dict: 
            start2junc_dict[start_posi] = []
            start2junc_dict[start_posi].append(SJ_posi)
            
        if start_posi in start2junc_dict: 
            if SJ_posi not in start2junc_dict[start_posi]:
                start2junc_dict[start_posi].append(SJ_posi)
                
        if end_posi not in end2junc_dict: 
            end2junc_dict[end_posi] = []
            end2junc_dict[end_posi].append(SJ_posi)
            
        if end_posi in end2junc_dict: 
            if SJ_posi not in end2junc_dict[end_posi]:
                end2junc_dict[end_posi].append(SJ_posi)

    
with open ("search_motif9.txt",'r') as hin:
            for line in hin:
                F = line.rstrip('\n').split('\t')
                abnormal_position = (F[5],str(int(F[8])-1),F[9])
                normal_sj = (F[5],F[2])
                
                if start2junc_dict.get(normal_sj) != None:
                    
                    for i in range(0,len(start2junc_dict.get(normal_sj))):
                        if normal_sj in start2junc_dict:
                            if start2junc_dict.get(normal_sj)[i] == abnormal_position: continue
                    
                            else:normal_position="\t".join(start2junc_dict.get(normal_sj)[i])
                    
                            print(normal_position  + '\t'+ F[0]+ '\t' + F[1] + '\t' + F[2]+ '\t' + F[3] + '\t' + F[4]+ '\t' + F[5] + '\t' + F[6]+ '\t' + F[7] + '\t' + F[8]+ '\t' + F[9] + '\t' + F[10]+ '\t' + F[11] + '\t' + F[12] + '\t' + F[13] + '\t' + F[14]+ '\t' + F[15] + '\t' + F[16]+ '\t' + F[17] + '\t' + F[18]+ '\t' + F[19] + '\t' + F[20]+ '\t' + F[21] + '\t' + F[22]+ '\t' + F[23] + '\t' + F[24] + '\t' + F[25] + '\t' + F[26]+ '\t' + F[27] + '\t' + F[28]+ '\t' + F[29] + '\t' + F[30])
                
                if end2junc_dict.get(normal_sj) != None:
                
                    for i in range(0,len(end2junc_dict.get(normal_sj))):
                    
                        if normal_sj in end2junc_dict:
                        
                            if end2junc_dict.get(normal_sj)[i] == abnormal_position: continue
                    
                            else:normal_position="\t".join(end2junc_dict.get(normal_sj)[i])
                    
                            print(normal_position  + '\t'+ F[0]+ '\t' + F[1] + '\t' + F[2]+ '\t' + F[3] + '\t' + F[4]+ '\t' + F[5] + '\t' + F[6]+ '\t' + F[7] + '\t' + F[8]+ '\t' + F[9] + '\t' + F[10]+ '\t' + F[11] + '\t' + F[12] + '\t' + F[13] + '\t' + F[14]+ '\t' + F[15] + '\t' + F[16]+ '\t' + F[17] + '\t' + F[18]+ '\t' + F[19] + '\t' + F[20]+ '\t' + F[21] + '\t' + F[22]+ '\t' + F[23] + '\t' + F[24] + '\t' + F[25] + '\t' + F[26]+ '\t' + F[27] + '\t' + F[28]+ '\t' + F[29] + '\t' + F[30])
                      