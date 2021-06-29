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
        m= re.match("(AC=\d*;)(AF=)(\d*.\d*)(;AN=\d*)",a)
        allele_frequency= m.group(3)
        print(f[0] + "\t" + f[1] +  "\t" + f[30] +  "\t" + normalSJ +  "\t" +  abnormal_SJ+  "\t" + f[31] +  "\t" + allele_frequency)
