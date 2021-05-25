import sys 
#python3 search_motif9.py > search_motif9.txt
#input_file = sys.argv[1]

donor_motif_list = [("d_e1","A"),("d_e2","G"),("d_i1","G"),("d_i2","T"),("d_i3","A"),("d_i3","G"),("d_i4","A"),("d_i5","G"),("d_i6","T")]

acceptor_motif_list =[("ac_i1","C"),("ac_i1","T"),("ac_i2","C"),("ac_i2","T"),("ac_i4","C"),("ac_i4","T"),("ac_i5","A"),("ac_i6","G"),("ac_e1","G")]

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

#with open("input_file",'r') as f:
with open("reverse_complement9.txt",'r') as f:

#with open("test430.txt",'r') as f:                
    
    for line in f:
        
        f = line.rstrip('\n').split('\t')
        
        #snp_position  = f[23],1st_int = f[5],2nd_int = f[6]
        
        if int(f[7]) == 1: #5⇨3の時
        
            if '*' in f[14]:   #変異が1st_intの時
                
                rd = int(f[23]) - int(f[5]) #relative difference
                
                donor53_rd_dict = {-2:"d_e1", -1:"d_e2", 0:"d_i1", 1:"d_i2", 2:"d_i3",3:"d_i4",4:"d_i5", 5:"d_i6"}
    
                value = donor53_rd_dict[rd] 
                
                #print(value)
                
                alt_base = f[26]
                
                snp_alt = (value, alt_base)
                
                #print(snp_alt)
                
                #donor_motif_list = [("d_e1","A"),("d_e2","G"),("d_i1","G"),("d_i2","T"),("d_i3","A"),("d_i3","G"),("d_i4","A"),("d_i5","G"),("d_i6","T")]
                
                #authentic_exon_position = int(f[6])+ 1 #後ろが正常だからexonは+1する。

                if snp_alt in donor_motif_list:
            
                #SNPの位置、SNPの塩基、正常exon、染色体・・・と続く
                    print((value) + '\t' + alt_base + '\t' + f[6] + '\t' + f[0] + '\t' + f[1] + '\t' + f[2] + '\t' + f[3] + '\t' + f[4] + '\t' + f[5] + '\t' + f[6] + '\t' + f[7] + '\t' + f[8] + '\t' + f[9] + '\t' + f[10] + '\t' + f[11] +'\t' + f[12] + '\t' + f[13] + '\t' + f[14] +'\t' + f[15] + '\t' + f[16] +'\t' +  f[17] + '\t' + f[18] + '\t' + f[19] + '\t' + f[20] + '\t' + f[21] + '\t' + f[22] + '\t' + f[23] + '\t' + f[24] + '\t' + f[25] + '\t' + f[26]+ '\t' + f[27])
                    
            elif '*' in f[18]:
                
                rd = int(f[23]) - int(f[6])
            
                acceptor53_rd_dict = {-5:"ac_i1", -4:"ac_i2", -3:"ac_i3", -2:"ac_i4", -1:"ac_i5",0:"ac_i6",1:"ac_e1"}
                
                value = acceptor53_rd_dict[rd]
            
                alt_base = f[26]
                
                snp_alt = (value, alt_base)
    
                authentic_exon_position = int(f[5])-1 #前が正常だからexonは-1する
                
                if snp_alt in acceptor_motif_list:
            
                    print((value) + '\t' + alt_base + '\t' + str(authentic_exon_position) + '\t' + f[0] + '\t' + f[1] + '\t' + f[2] + '\t' + f[3] + '\t' + f[4] + '\t' + f[5] + '\t' + f[6] + '\t' + f[7] + '\t' + f[8] + '\t' + f[9] + '\t' + f[10] + '\t' + f[11] +'\t' + f[12] + '\t' + f[13] + '\t' + f[14] +'\t' + f[15] + '\t' + f[16] +'\t' +  f[17] + '\t' + f[18] + '\t' + f[19] + '\t' + f[20] + '\t' + f[21] + '\t' + f[22] + '\t' + f[23] + '\t' + f[24] + '\t' + f[25] + '\t' + f[26]+ '\t' + f[27])
                    
        elif int(f[7]) == 2:
            
            if '*' in f[18]:    #2つ目が変異:ドナー
                
                rd = int(f[23]) - int(f[6])
                
                donor35_rd_dict = {2:"d_e1", 1:"d_e2", 0:"d_i1",-1:"d_i2", -2:"d_i3", -3:"d_i4", -4:"d_i5", -5:"d_i6"} 
                
                #donor35_rd_dict = {2:"d_e1", 1:"d_e1", 0:"d_i1",-1:"d_i2", -2:"d_i3", -3:"d_i4", -4:"d_i5", -5:"d_i6"} 
                 
                value = donor35_rd_dict[rd]
                
                base= f[26]
                
                alt_base = complement.get(base)
                
                snp_alt = (value, alt_base)
                
                authentic_exon_position = int(f[5])-1 #前が正常だからexonは-1する
                
                if snp_alt in donor_motif_list:
            
                    print((value) + '\t' + alt_base + '\t' + str(authentic_exon_position) + '\t' + f[0] + '\t' + f[1] + '\t' + f[2] + '\t' + f[3] + '\t' + f[4] + '\t' + f[5] + '\t' + f[6] + '\t' + f[7] + '\t' + f[8] + '\t' + f[9] + '\t' + f[10] + '\t' + f[11] +'\t' + f[12] + '\t' + f[13] + '\t' + f[14] +'\t' + f[15] + '\t' + f[16] +'\t' +  f[17] + '\t' + f[18] + '\t' + f[19] + '\t' + f[20] + '\t' + f[21] + '\t' + f[22] + '\t' + f[23] + '\t' + f[24] + '\t' + f[25] + '\t' + f[26]+ '\t' + f[27])
                    
                    
            elif '*' in f[14]:
                
                rd = int(f[23]) - int(f[5])
                
                acceptor35_rd_dict = {5:"ac_i1", 4:"ac_i2", 3:"ac_i3",2:"ac_i4", 1:"ac_i5",0:"ac_i6",-1:"ac_e1"}
            
                #if rd == 3:continue
            
                value = acceptor35_rd_dict[rd]
                
                base= f[26]
                
                alt_base = complement.get(base)
                
                snp_alt = (value, alt_base)
                
                #ここ、3→5の時は、DNAのREF　ALTがたとえば、C→Tなら、RNAは、G⇨Aだから、それがモチーフに対してどうかをみないと行けない。
                
                #authentic_exon_position = int(f[6])+ 1 #後ろが正常だからexonは+1する。
                
                if snp_alt in acceptor_motif_list:
            
                    print((value) + '\t' + alt_base + '\t' + f[6] + '\t' + f[0] + '\t' + f[1] + '\t' + f[2] + '\t' + f[3] + '\t' + f[4] + '\t' + f[5] + '\t' + f[6] + '\t' + f[7] + '\t' + f[8] + '\t' + f[9] + '\t' + f[10] + '\t' + f[11] +'\t' + f[12] + '\t' + f[13] + '\t' + f[14] +'\t' + f[15] + '\t' + f[16] +'\t' +  f[17] + '\t' + f[18] + '\t' + f[19] + '\t' + f[20] + '\t' + f[21] + '\t' + f[22] + '\t' + f[23] + '\t' + f[24] + '\t' + f[25] + '\t' + f[26]+ '\t' + f[27])
                    
                    
                    