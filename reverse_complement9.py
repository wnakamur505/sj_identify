import sys 

with open("fetch_motif_sequence.txt",'r') as f:  
    
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
         
    for line in f:
        
        f = line.rstrip('\n').split('\t')
        
        bases = f[0]

        if int(f[6]) == 1:
        
            print(f[0] + '\t' + f[0] + '\t' +f[1] + '\t' + f[2] + '\t' + f[3] + '\t' + f[4] + '\t' + f[5] + '\t' + f[6] + '\t' + f[7] + '\t' + f[8] + '\t' + f[9] + '\t' + f[10] + '\t' + f[11] +'\t' + f[12] + '\t' + f[13] + '\t' + f[14] +'\t' + f[15] + '\t' + f[16] +'\t' +  f[17] + '\t' + f[18] + '\t' + f[19] + '\t' + f[20] + '\t' + f[21] + '\t' + f[22] + '\t' + f[23] + '\t' + f[24] + '\t' + f[25] + '\t' + f[26] )
            
        if int(f[6]) == 2:
        
            bases = reversed ([complement.get(base,base) for base in bases])
            
            print( ''.join(bases)+ '\t' + f[0] + '\t' + f[1] + '\t' + f[2] + '\t' + f[3] + '\t' + f[4] + '\t' + f[5] + '\t' + f[6] + '\t' + f[7] + '\t' + f[8] + '\t' + f[9] + '\t' + f[10] + '\t' + f[11] +'\t' + f[12] + '\t' + f[13] + '\t' + f[14] +'\t' + f[15] + '\t' + f[16] +'\t' +  f[17] + '\t' + f[18] + '\t' + f[19] + '\t' + f[20] + '\t' + f[21] + '\t' + f[22] + '\t' + f[23] + '\t' + f[24] + '\t' + f[25] + '\t' + f[26] )