import sys
input_file = sys.argv[1]

with open(input_file,"r") as hin:

    for line in hin:
        
        f = line.rstrip('\n').split('\t')
        
        if not f[0].startswith("206"):continue
        
        print(f)