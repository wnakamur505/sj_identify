#python3 all_information_include_authentic_SJ9.py > all_information_include_authentic_SJ9.txt
with open("get_authentic_SJ_from_junctionDB9.txt",'r') as hin:
#with open("test50755.txt",'r') as hin:

    for line in hin:
        
        if "None None" in line:continue
    
        f = line.rstrip('\n').split('\t')
        
        F = f[0].replace("None","").replace("(",'').replace(")",',').rstrip('\n').split(',') #replace("'","") #この真ん中のreplace(")",',')が大事。
        #Fは下記がごちゃまぜ
        
        Chr_num = F[0].replace("'","").replace(' ','')

        autentic_start_position = F[1].replace("'","").replace(' ','')

        autentic_end_position = F[2].replace("'","").replace(' ','')

        SNP_relative_position = F[3].replace(' ','')
        
        print (Chr_num +  '\t' + autentic_start_position +  '\t' + autentic_end_position +  '\t' + SNP_relative_position + '\t' + f[1] + '\t' + f[2]+ '\t' + f[3] + '\t' + f[4]+ '\t' + f[5] + '\t' + f[6]+ '\t' + f[7] + '\t' + f[8]+ '\t' + f[9] + '\t' + f[10]+ '\t' + f[11] + '\t' + f[12] + '\t' + f[13] + '\t' + f[14]+ '\t' + f[15] + '\t' + f[16]+ '\t' + f[17] + '\t' + f[18]+ '\t' + f[19] + '\t' + f[20]+ '\t' + f[21] + '\t' + f[22]+ '\t' + f[23] + '\t' + f[24] + '\t' + f[25] + '\t' + f[26]+ '\t' + f[27] + '\t' + f[28]+ '\t' + f[29] + '\t' + f[30])