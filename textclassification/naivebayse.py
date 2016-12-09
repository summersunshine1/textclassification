# -*- coding: UTF-8 -*-

def getcw():
    rootdir = "F:\\dataset"
    dir = os.walk(rootdir)
    totalcw=[]
    print("read doc begin")
    for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        cw=[]#represent doc belong to one catogory
        for filename in filenames:#输出文件信息 
            path_name=os.path.join(parent,filename)
            file_object = codecs.open(path_name,'r','utf-8')
            try:
                all_the_text = file_object.read()
            finally:
                file_object.close()
            arr=all_the_text.split()
            tempw=[]
            for wa in arr:
                tempw.append(wa)
            cw.append(tempw)
        if not len(cw)==0:
            totalcw.append(cw)
    return totalcw

def getvocab():
    file_object = codecs.open("F:/vocab.txt",'r','utf-8')
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()
    v = all_the_text.split()
    return v  
                
def naivebayse():
    v = getvocab()
    cw = getcw()
    cnum=len(cw)
    count=[]
    f=[]
    c=[]#compute each class ratio
    totalword=0
    for i in range(cnum):
        n=len(cw[i])
        for j in range(n):
            tempw=cw[i][j]
            totalword += len(tempw)
     
    for i in range(cnum):
        count.append([0]*len(v))
        f.append([0]*len(v))
        c.append(0)
    for i in range(cnum):
        n=len(cw[i])
        #compute each topic each vocab count
        classword=0
        for j in range(n):
            tempw=cw[i][j]
            for k in range(len(tempw)):
                word=tempw[k]
                if not word in v:
                    continue
                windex=v.index(word)
                count[i][windex]+=1
                classword+=1
        #compute each topic each vocab frequency
        for j in range(len(v)):
            f[i][j]=(count[i][j]+1)/(v+classword)
        c[i] = classword/totalword
    return f,c
            
 def train(traindocs,f,c):
    n = len(traindocs)
    v = getvocab()
    classifyresult = []
    cnum = len(c)
    for i in range(n):
        doc = traindocs[i]
        m = len(doc)
        cmaxprob = 0
        cmaxindex = 0
        for j in range(cnum):
            prob=c[j]
            for k in range(m):
                word = doc[k]
                if not word in v:
                    continue
                wordindex = v.index(word)
                prob = prob*f[j][wordindex]
            if prob>cmaxprob:
                cmaxprob = prob
                cmaxindex = j
        classifyresult.append(cmaxindex)
    return classifyresult
        
                
            
            
            
        
    
    
    
    
    
        
    
        
            
            
            
            
            
            
            
    
             
        