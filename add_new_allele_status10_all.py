import glob

input_files = glob.glob("add_new_allele_status10_chr*.txt")

for line in input_files:
    
    with open(line,"r") as f: 
        
        for line in f:
            
            f = line.rstrip('\n').split('\t')
        
            if f[0].startswith("{"):continue
        
            print("\t".join(f))