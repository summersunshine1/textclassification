# -*- coding: UTF-8 -*-

def getcw(w,topicsnum):
    m=len[w]
    cw=[]
    j=0
    curtopicnum=topicsnum[0]
    curtopic=0
    for i in range(m):
        if j==curtopicnum:
            j=0
            curtopic+=1
            curtopicnum=topicsnum[curtopic]
        cw[curtopic].append(w[i])
        j+=1
    return cw
    
    
def naivebayse(w,v,topicsnum):
    cw = getcw(w,topicsnum)
    tnum = len(topicsnum)
    cnum=len(cw)
    count=[]
    f=[]
    for i in range(tnum):
        count.append([0]*len(v))
        f.append([0]*len(v))
    for i in range(cw):
        n=len(cw[i])
        #compute each topic each vocab count
        totalword=0
        for j in range(n):
            tempw=cw[i][j]
            for k in range(len(tempw)):
                word=tempw[k]
                windex=v.index(word)
                count[i][windex]+=1
                totalword+=1
        #compute each topic each vocab frequency
        for j in range(len(v)):
            f[i][j]=(count[i][j]+1)/(v+totalword)
    return f[i][j]
            
        
        
            
            
            
            
            
            
            
    
             
        