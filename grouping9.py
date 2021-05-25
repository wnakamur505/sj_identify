with open("all_information_include_authentic_SJ9.txt",'r') as hin:
#with open("test_all_info.txt",'r') as hin:
#python3 grouping9.py > grouping9.txt

        for i,name in enumerate(hin,1): #i：インデックスが入る変数、#name；要素が入る変数、#hin：配列
        
            #print("group_number = {:03} info={}".format(i,name))
            f = str(i) + '\t' + name
            F = f.rstrip('\n')
            print(F)
            
        """
        website:【python】enumerate関数の使い方（インデックス番号と要素を取り出す
        f = line.rstrip('\n').split('\t')
        
        """