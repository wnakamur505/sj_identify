# python3 test_get_authentic_SJ_fromDB.py > test_get_authentic_SJ_fromDB14.txt
start2junc_dict = {}
end2junc_dict = {}

start2junc_list =[]
end2junc_list = []

with open ("screening_junctionDB.txt",'r') as hin:
#with open ("test_screening_junctionDB3.txt",'r') as hin:

    for line in hin:
    
        f = line.rstrip('\n').split('\t')
        
        start_posi = (f[0],f[1])
        end_posi = (f[0],f[2])
        SJ_posi = (f[0],f[1],f[2])
        
        
        if start_posi not in start2junc_dict:
            start2junc_dict[start_posi]=SJ_posi
            
        elif (SJ_posi != start2junc_dict.get(start_posi)) and ([(start_posi),[SJ_posi]] not in start2junc_list):
            start2junc_list.append([(start_posi),[SJ_posi]])
        
        if end_posi not in end2junc_dict:
            end2junc_dict[end_posi]=SJ_posi
            
        elif (SJ_posi != end2junc_dict[end_posi]) and ([(end_posi),[SJ_posi]] not in end2junc_list):
            end2junc_list.append([(end_posi),[SJ_posi]])
            
    #for i in range(0,len(end2junc_list)):
        #print(end2junc_list[i][0])
    #print(end2junc_dict)    
    
        
with open ("search_motif9.txt",'r') as hin:
#with open ("search_motif9_tail.txt",'r') as hin:
    #d_i3	G	129880562	AGGTATTT	AAATACCT	chr3	129888976	129888983	129880563	129888981	2	2	1	Intronic alternative 5'SS	---	TMCC1(NM_001349264);TMCC1(NM_001349271);TMCC1(NM_001349275)	1;1;1	s;s;s	0;0;0	TMCC1(NM_001349264);TMCC1(NM_001349271);TMCC1(NM_001349275)	*;*;*	*;*;*	*;*;*	36	chr3	129888978	129888979	rs12638238	T	C	AC=519;AF=0.103634;AN=5008;NS=2504;DP=21652;EAS_AF=0.1835;AMR_AF=0.1254;AFR_AF=0.0303;EUR_AF=0.0944;SAS_AF=0.1145;AA=T|||;VT=SNP

    for line in hin:
    
        F = line.rstrip('\n').split('\t')
        abnormal_position = (F[5],str(int(F[8])-1),F[9])
        normal_sj = (F[5],F[2]) #(chr3,129880562):
        #start2junc_gict.get("chr3","129880562") → chr3	129880562	129888981

        #print("1")
        #print(start2junc_dict.get(normal_sj))
        #print(abnormal_position)
        #print("continue")
        
        if start2junc_dict.get(normal_sj) == abnormal_position:continue
                
            #SJ_posi = (f[0],f[1],f[2])が呼ばれる、
        if end2junc_dict.get(normal_sj) == abnormal_position:continue 
             
        if normal_sj in start2junc_dict:
            normal_position="\t".join(start2junc_dict.get(normal_sj))
            print(normal_position  + '\t'+ F[0]+ '\t' + F[1] + '\t' + F[2]+ '\t' + F[3] + '\t' + F[4]+ '\t' + F[5] + '\t' + F[6]+ '\t' + F[7] + '\t' + F[8]+ '\t' + F[9] + '\t' + F[10]+ '\t' + F[11] + '\t' + F[12] + '\t' + F[13] + '\t' + F[14]+ '\t' + F[15] + '\t' + F[16]+ '\t' + F[17] + '\t' + F[18]+ '\t' + F[19] + '\t' + F[20]+ '\t' + F[21] + '\t' + F[22]+ '\t' + F[23] + '\t' + F[24] + '\t' + F[25] + '\t' + F[26]+ '\t' + F[27] + '\t' + F[28]+ '\t' + F[29] + '\t' + F[30])
                   
        if normal_sj in end2junc_dict:
            normal_position="\t".join(end2junc_dict.get(normal_sj))

            print(normal_position  + '\t'+ F[0]+ '\t' + F[1] + '\t' + F[2]+ '\t' + F[3] + '\t' + F[4]+ '\t' + F[5] + '\t' + F[6]+ '\t' + F[7] + '\t' + F[8]+ '\t' + F[9] + '\t' + F[10]+ '\t' + F[11] + '\t' + F[12] + '\t' + F[13] + '\t' + F[14]+ '\t' + F[15] + '\t' + F[16]+ '\t' + F[17] + '\t' + F[18]+ '\t' + F[19] + '\t' + F[20]+ '\t' + F[21] + '\t' + F[22]+ '\t' + F[23] + '\t' + F[24] + '\t' + F[25] + '\t' + F[26]+ '\t' + F[27] + '\t' + F[28]+ '\t' + F[29] + '\t' + F[30])
                
            
                #print(normal_sj) ('chr5', '55267137')
                #print(start2junc_list[i]):[('chr1', '1312949'), [('chr1', '1312949', '1313034')]]
                #print(start2junc_list[i][1][0])：('chr1', '779092', '803918')
                #print(start2junc_list[i][0])：('chr1', '779092')
            #print(start2junc_dict) #：('chr1', '779092'): ('chr1', '779092', '803918') これあれば、リストからぬく、これは次で・
            #('chr1', '30039'): ('chr1', '30039', '30563'),
            #print(normal_sj):('chr1', '1040664')
            #print(start2junc_dict.get(normal_sj) # KeyError: ('chr1', '1040664')
            
        for i in range(0,len(start2junc_list)):
                    #print(normal_sj) 
                    #print(start2junc_list[i][0])
                    #print(start2junc_dict[normal_sj])なぜこれがだめ？
            #if start2junc_dict.get(normal_sj) == start2junc_list[i][1][0]:continue #これはもはや不要のはず。後で消す。
            
            if start2junc_list[i][1][0] == abnormal_position:continue
            
            #print("abnormal_position",abnormal_position)
            #print("start2junc_list[i][1]",start2junc_list[i][1])
            #print("start2junc_list[i][1][0]",start2junc_list[i][1][0])
            #start2junc_list[i][1][0] ('chr1', '3900631', '3903964')
            #if start2junc_list[i][1][0] == start2junc_dict.get(normal_sj):continue
        
            #if start2junc_list[i] in start2junc_list:continue
            #start2junc_gict.get("chr3","129880562") → chr3	129880562	129888981

            if normal_sj == start2junc_list[i][0] :
            
                normal_position="\t".join(start2junc_list[i][1][0])
                        #print("start2junc_listから")

                print(normal_position + '\t'+ F[0]+ '\t' + F[1] + '\t' + F[2]+ '\t' + F[3] + '\t' + F[4]+ '\t' + F[5] + '\t' + F[6]+ '\t' + F[7] + '\t' + F[8]+ '\t' + F[9] + '\t' + F[10]+ '\t' + F[11] + '\t' + F[12] + '\t' + F[13] + '\t' + F[14]+ '\t' + F[15] + '\t' + F[16]+ '\t' + F[17] + '\t' + F[18]+ '\t' + F[19] + '\t' + F[20]+ '\t' + F[21] + '\t' + F[22]+ '\t' + F[23] + '\t' + F[24] + '\t' + F[25] + '\t' + F[26]+ '\t' + F[27] + '\t' + F[28]+ '\t' + F[29] + '\t' + F[30])
                        
        for i in range(0,len(end2junc_list)):
            
            #if end2junc_dict.get(normal_sj) == end2junc_list[i][1][0]:continue #すでにディクショナリーのvalueと同じものが、listの後ろの要素に入っているならスルー。
            if end2junc_list[i][1][0] == abnormal_position:continue
                
            #if end2junc_list[i] in end2junc_list:continue
            if normal_sj == end2junc_list[i][0]:
                
                normal_position="\t".join(end2junc_list[i][1][0])
                        #print("start2junc_dictから")

                print(normal_position + '\t'+ F[0]+ '\t' + F[1] + '\t' + F[2]+ '\t' + F[3] + '\t' + F[4]+ '\t' + F[5] + '\t' + F[6]+ '\t' + F[7] + '\t' + F[8]+ '\t' + F[9] + '\t' + F[10]+ '\t' + F[11] + '\t' + F[12] + '\t' + F[13] + '\t' + F[14]+ '\t' + F[15] + '\t' + F[16]+ '\t' + F[17] + '\t' + F[18]+ '\t' + F[19] + '\t' + F[20]+ '\t' + F[21] + '\t' + F[22]+ '\t' + F[23] + '\t' + F[24] + '\t' + F[25] + '\t' + F[26]+ '\t' + F[27] + '\t' + F[28]+ '\t' + F[29] + '\t' + F[30])