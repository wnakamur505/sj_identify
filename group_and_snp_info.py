list=[]
dict={}
list={}

#with open("test_additional_SNP_information.txt","r") as hin:
with open("additional_SNP_information.txt","r") as hin:
 
    for line in hin:
        f = line.rstrip('\n').split('\t')
        group_id1 = f[0]
        SJ_info = (f[0],f[1],f[2],f[3],f[4],f[5],f[6])
        dict[SJ_info]= group_id1
        #print(dict)
        #{('chr19', '5928174', '45630159', '45630484', 'rs274793', '0.714657'): '265'}
        #{('chr19', '5928174', '45630159', '45630484', 'rs274793', '0.714657'): '266'}
        
#with open("test_add_new_allele_status_all_zero11_included.txt","r") as hin:
with open("add_new_allele_status_all_zero11_included.txt","r") as hin:

    for line in hin:
        F = line.rstrip('\n').split('\t')
        group_id2 = F[0] #265
        SNP_info = [F[1],F[2],F[3],F[4],F[5]] #['NA20756', 'ERR188251', '0', '0', '0|0]
        
        for key in dict:
            value = dict[key]

            if value == group_id2:
                a, b, c, d, e, f, g = key
                print(group_id2 + "\t" + SNP_info[0] + "\t" + SNP_info[1] + "\t" + SNP_info[2] + "\t" + SNP_info[3] + "\t" +  SNP_info[4] +  "\t" + b  +  "\t" + c  +  "\t" + d  +  "\t" + e  +  "\t" + f  +  "\t" + g)
                
                
            