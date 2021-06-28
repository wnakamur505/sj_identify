import re
with open("grouping10.txt","r") as hin: 

    for line in hin:
        
        f = line.rstrip('\n').split('\t')
        
        if f[26] == "*":
        
            normalSJ = f[12]
        
            abnormal_SJ = f[13]
            
    
        if f[22] == "*":
            
            normalSJ = f[13]
        
            abnormal_SJ = f[12]

        
        a = str(f[34])
        #print(a)
        #AC=1298;AF=0.259185;AN=5008;NS=2504;DP=19706;EAS_AF=0.1508;AMR_AF=0.2378;AFR_AF=0.4433;EUR_AF=0.2584;SAS_AF=0.138;AA=T|||;VT=SNP
        #print(b) #483, ERR188320
        
        #python3 test5234.py ('483', 'ERR188406')
        m= re.match("(AC=\d*;)(AF=)(\d*.\d*)(;AN=\d*)",a)
        #print(m)

        #m= re.match("(\d*)\, (ERR\d*)",b)
        #print(m)
        allele_frequency= m.group(3)
        
        print(f[0] + "\t" + f[1] +  "\t" + f[30] +  "\t" + normalSJ +  "\t" +  abnormal_SJ+  "\t" + f[31] +  "\t" + allele_frequency)
