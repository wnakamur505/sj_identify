remove_dup_dict ={}
sample_count={}
duplicated_sample_id_count =[]

with open ("remove_dup.txt","r") as hin:
    for line in hin:
        f = line.rstrip('\n').split('\t')
        sample_number=f[0]
        run_number=f[1]
        remove_dup_dict[run_number] = sample_number

with open ("short_SraRunTable.txt","r") as hin:

    for line in hin:
        f = line.rstrip('\n').split('\t')
        if f[0].startswith("Run"):continue
        run_id =f[0]
        sample_id = f[1].replace("GEUV:","")
        
        if sample_id not in sample_count:
            sample_count[sample_id] = 0
        sample_count[sample_id] = sample_count[sample_id] +1
        
    for sample2_id in sample_count:
        if sample_count[sample2_id] < 2:continue
        duplicated_sample_id_count.append(sample2_id)
        
    for i in range(0,len(duplicated_sample_id_count)):
        duplicated_sample_id= duplicated_sample_id_count[i]
        print(remove_dup_dict[duplicated_sample_id])
    
    for sample2_id in sample_count:
        if sample_count[sample2_id] < 2:
            print(remove_dup_dict[sample2_id])