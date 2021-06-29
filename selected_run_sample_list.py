import glob

sample_list =[]
key_count = {}


with open("select_sample_considered_duplication.txt","r") as hin:

    for line in hin:
        f = line.rstrip('\n').split('\t')
        ERR_id = f[0]
        
        files = glob.glob("/home/ubuntu/environment/current_issue/junc_utils/sen_genome/" + ERR_id + "/star/" + ERR_id + ".SJ.out.annot.tab")
        #files = glob.glob(ERR_id + "/star/" + ERR_id + ".SJ.out.annot.tab")
        
        for line in files:
            with open(line,"r") as hin:
                for line in hin:
                    f =line.rstrip('\n').split('\t')

                    if f[9] not in ["Alternative 3'SS","Alternative 5'SS","Intronic alternative 3'SS","Intronic alternative 5'SS"]:continue 
            
                    key = f[0] + '\t' + f[1] + '\t' + f[2] + '\t' + f[3] + '\t' + f[4] + '\t' + f[5] + '\t' + f[9] + '\t' + f[10] + '\t' + f[11] +'\t' + f[12] + '\t' + f[13] + '\t' + f[14] +'\t' + f[15] + '\t' + f[16] +'\t' +  f[17] + '\t' + f[18]
            
                    if key not in key_count:
                        key_count[key] = 0
            
                    key_count[key] = key_count[key] +1
            
    for key in key_count:
                
        print(key + '\t' + str(key_count[key]))