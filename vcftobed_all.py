import re

with open("ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.vcf","r") as f:

    for line in f:

        f = line.rstrip('\n').split('\t')
        
        if f[0].startswith('#') : continue
        
        if len(f[3]) != 1: continue 
    
        if len(f[4]) != 1: continue 
        
        h = re.search(r"(;AF=)+(\d+\.?\d*)+(;AN=)", f[7])
        k = h.group()
        p = re.sub(";AF=", "", k)
        n = re.sub(";AN=", "", p)
        
        if float(n) < 0.05: continue
        
        print ("chr"+ f[0] + '\t' + str(int(f[1]) - 1) + '\t' + f[1] + '\t' + f[2]+ '\t' +f[3]+ '\t' +f[4]+ '\t'+f[7])