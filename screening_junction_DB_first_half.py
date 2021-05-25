import sys 
input_file = sys.argv[1] #"wgEncodeGencodeBasicV37.txt"
#screening_junction_DB_first_half.py

with open(input_file,"r") as f:

    for line in f:
        
        f = line.rstrip('\n').split('\t')
        chr = f[2]
        number_of_exon= f[8]
        if int(number_of_exon) <2:continue
        
        start_position = f[9].replace(',','\t')
        
        end_position = f[10].replace(',','\t')
        
        print(number_of_exon + '\t'+ chr + '\t'+ start_position + end_position)