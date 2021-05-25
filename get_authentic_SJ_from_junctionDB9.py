# python3 get_authentic_SJ_from_junctionDB.py > get_authentic_SJ_from_junctionDB3.txt
start2junc = {}
end2junc = {}

with open ("screening_junctionDB.txt",'r') as hin:

    for line in hin:
    
        f = line.rstrip('\n').split('\t')
     
        start2junc[(f[0],f[1])]=(f[0],f[1],f[2])
        
        end2junc[(f[0],f[2])]=(f[0],f[1],f[2])
        
        
    with open ("search_motif9.txt",'r') as hin:

        for line in hin:
    
            F = line.rstrip('\n').split('\t')
            #print(F[30]) これラスト
            print(start2junc.get((F[5],F[2])), end2junc.get((F[5],F[2])),F[0] + '\t' + F[1] + '\t' + F[2]+ '\t' + F[3] + '\t' + F[4]+ '\t' + F[5] + '\t' + F[6]+ '\t' + F[7] + '\t' + F[8]+ '\t' + F[9] + '\t' + F[10]+ '\t' + F[11] + '\t' + F[12] + '\t' + F[13] + '\t' + F[14]+ '\t' + F[15] + '\t' + F[16]+ '\t' + F[17] + '\t' + F[18]+ '\t' + F[19] + '\t' + F[20]+ '\t' + F[21] + '\t' + F[22]+ '\t' + F[23] + '\t' + F[24] + '\t' + F[25] + '\t' + F[26]+ '\t' + F[27] + '\t' + F[28]+ '\t' + F[29] + '\t' + F[30])

        #python3 get_authentic_SJ_from_junctionDB9.py > get_authentic_SJ_from_junctionDB9.txt
        
        
