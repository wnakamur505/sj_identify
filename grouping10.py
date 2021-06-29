with open("get_authentic_SJ_fromDB627.txt",'r') as hin:

        for i,name in enumerate(hin,1): 
            f = str(i) + '\t' + name
            F = f.rstrip('\n')
            print(F)