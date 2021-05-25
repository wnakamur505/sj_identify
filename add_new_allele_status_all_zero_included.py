import re
conversion_dict={}

with open ("SraRunTable.txt","r") as hin:

    for line in hin:
        
        f = line.rstrip('\n').split('\t')
        
        if f[0].startswith("Run"):continue
        
        err_id =f[0]
        
        hg_id = f[1].replace("GEUV:","")
        
        conversion_dict[err_id] = hg_id
        
with open("add_ERR_zero.txt","r") as hin:
    for line in hin:
        f = line.rstrip('\n').split('\t')
        a = str(f[0])
        b = a.replace("'","").replace("(","").replace(")","")
        #print(b) #483, ERR188320
        
        #python3 test5234.py ('483', 'ERR188406')
        
        m= re.match("(\d*)\, (ERR\d*)",b)
        #print(m)
        group_id = m.group(1)
        run_id = m.group(2)
        
        sample_id = conversion_dict[run_id]
        
        #print(group_id + "\t" + sample_id + "\t" + run_id + "\t" + "0" + "\t" + "0" + "\t" + "0|0")
        
with open("add_new_allele_status9_all.txt","r") as hin:

    for line in hin:
        
        f = line.rstrip('\n').split('\t')
        
        print(f[0]+ "\t" + f[1]+ "\t" + f[2]+ "\t" + f[3]+ "\t" + f[4]+ "\t" + f[5])
        
