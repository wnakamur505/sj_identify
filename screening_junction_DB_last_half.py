import sys 
input_file = sys.argv[1] #screening_junctionDB_first_half.txt
#screening_junction_DB_last_half.py

with open(input_file,"r") as f:
    
    for line in f:
        
        F= line.rstrip('\n').split('\t')
        
        n= int(F[0])

        for i in range(n+2,2*n+1):
            
            print(F[1] +'\t' + F[i] +'\t' + F[i-n+1])