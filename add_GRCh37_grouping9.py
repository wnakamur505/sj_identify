GRCh37_dict={}

#with open("testGRCh37.bed","r") as hin: 
with open("GRCh37_ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.bed","r") as hin: 
  
    for line in hin:
    
        f = line.rstrip('\n').split('\t')
        
        GRCh37_position = [f[1],f[2]]
        
        GRCh37_dict[f[3]] = GRCh37_position
    
    
#with open("grouping9.txt","r") as hin:
with open("grouping10.txt","r") as hin:
             
    for line in hin:
    
        F = line.rstrip('\n').split('\t')
            
        id = F[31]
                
        if id not in GRCh37_dict:continue
                
        if id in GRCh37_dict:
                
                
            positions = GRCh37_dict[id]
            
            F2 = "\t".join(F) + '\t' + "\t".join(positions)
              
            print(F2)
            #python3 add_GRCh37_grouping9.py > add_GRCh37_grouping9.txt
            #wc grouping2.txt
            #wc add_GRCh37_grouping3.txt
            #wc add_GRCh37_grouping9.txt