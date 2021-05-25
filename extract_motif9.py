with open("selected_run_sample_list.txt","r") as f:
    for line in f:
        
        f = line.rstrip('\n').split('\t')
        
        if int(f[16]) < 30: continue
        
        if int(f[3]) == 1:
        
            if '*' in f[10]: #strand:+ 5'SS
            
                on= f[11].split(';',2)  #on means offset_number
                
                if on[0] == '*':
                    on[0] = 0

                
                int_sta_posi = str(int(f[1])-2-int(on[0])) #intron_start_posion
                
                int_end_posi = str(int(f[1])+5-int(on[0]))
                
                key = f[0] + '\t' + int_sta_posi +'\t' + int_end_posi + '\t' + f[1] +'\t' + f[2] +'\t' + f[3] +'\t'+ f[4] +'\t' + f[5] + '\t'+ f[6] +'\t' + f[7]+ '\t' +f[8]+ '\t' + f[9] + '\t' + f[10] + '\t' + f[11] +'\t' + f[12] + '\t' + f[13] + '\t' + f[14] +'\t' + f[15] +'\t' + f[16]

                print(key)
        
                
            elif '*' in f[14]:#strand:+ 3'SS
                
                on = f[15].split(';',2) 
                
                if on[0] == '*':
                    on[0] = 0
              
                int_sta_posi = str(int(f[2])-5-int(on[0]))
                
                int_end_posi = str(int(f[2])+1-int(on[0]))
                
                
                key = f[0] + '\t' + int_sta_posi +'\t' + int_end_posi + '\t' + f[1] +'\t' + f[2] +'\t' + f[3] +'\t'+ f[4] +'\t' + f[5] + '\t'+ f[6] +'\t' + f[7]+ '\t' +f[8]+ '\t' + f[9] + '\t' + f[10] + '\t' + f[11] +'\t' + f[12] + '\t' + f[13] + '\t' + f[14] +'\t' + f[15] +'\t' + f[16]
                
                print(key)
                
                
                
        if int(f[3]) == 2:
            
            if '*' in f[10]: #strand:- 5'SS
                
                on = f[11].split(';',2) 
                
                if on[0] == '*':
                    on[0] = 0
                
                int_sta_posi = str(int(f[1])-1-int(on[0]))
                
                int_end_posi = str(int(f[1])+5-int(on[0]))
                    
                key = f[0] + '\t' + int_sta_posi +'\t' + int_end_posi + '\t' + f[1] +'\t' + f[2] +'\t' + f[3] +'\t'+ f[4] +'\t' + f[5] + '\t'+ f[6] +'\t' + f[7]+ '\t' +f[8]+ '\t' + f[9] + '\t' + f[10] + '\t' + f[11] +'\t' + f[12] + '\t' + f[13] + '\t' + f[14] +'\t' + f[15] +'\t' + f[16]
                
                print(key)
                
                
            elif '*' in f[14]: #strand:- 3'SS
                
                on = f[15].split(';',2)  
                
                if on[0] == '*':
                    on[0] = 0
                
                int_sta_posi = str(int(f[2])-5-int(on[0]))
                
                int_end_posi = str(int(f[2])+2-int(on[0]))
                
                key = f[0] + '\t' + int_sta_posi +'\t' + int_end_posi + '\t' + f[1] +'\t' + f[2] +'\t' + f[3] +'\t'+ f[4] +'\t' + f[5] + '\t'+ f[6] +'\t' + f[7]+ '\t' +f[8]+ '\t' + f[9] + '\t' + f[10] + '\t' + f[11] +'\t' + f[12] + '\t' + f[13] + '\t' + f[14] +'\t' + f[15] +'\t' + f[16]
               
                print (key)
        
