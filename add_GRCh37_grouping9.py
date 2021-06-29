GRCh37_dict={}

with open("GRCh37_ALL.wgs.phase3_shapeit2_mvncall_integrated_v5b.20130502.sites.bed","r") as hin: 
  
    for line in hin:
    
        f = line.rstrip('\n').split('\t')
        
        GRCh37_position = [f[1],f[2]]
        
        GRCh37_dict[f[3]] = GRCh37_position
    
    
with open("grouping10.txt","r") as hin:
             
    for line in hin:
    
        F = line.rstrip('\n').split('\t')
            
        id = F[31]
                
        if id not in GRCh37_dict:continue
                
        if id in GRCh37_dict:
                
                
            positions = GRCh37_dict[id]
            
            F2 = "\t".join(F) + '\t' + "\t".join(positions)
              
            print(F2)