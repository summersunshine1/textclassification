# -*- coding: UTF-8 -*-
import os
import codecs
import math

def frequency(t,w):
    alpha=0
    m=len(w)
    for i in range(m):
        dic = dict()
        wordarr=w[i]
        n=len(wordarr)
        for j in range(n):
            word=wordarr[j]
            if word==t:
                if word in dic:
                    dic[word]+=1
                else:
                    dic[word]=1
        for k,v in dic.items():
            alpha=alpha+v/n
    return alpha
        
def accuracy(M,A,B):
    beta=math.pow(M,A/(A+B))
    return beta
    
def chi(t,c,totalcw):
    A=0
    B=0
    C=0
    D=0
    m=len(totalcw)
    for i in range(m):
        w=totalcw[i]
        n=len(w)
        if i==c:
            for j in range(n):
                if t in w[j]:
                    A+=1
                else:
                    C+=1
        else:
            for j in range(n):
                if t in w[j]:
                    B+=1
                else:
                    D+=1       
    
    re=(A*D-B*C)/((A+B)*(C+D))
    return A,B,re

def create_txt(file_path, vocabarr):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for word in vocabarr:
        f.write(word)
        f.write('\n')
    f.close()
    
def getcw(catagory):
    rootdir = "F:\\dataset"
    dir = os.walk(rootdir)
    totalcw=[]
    totaldoc=0
    wordset=set()#store dict words
    print("read doc begin")
    for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        cw=[]#represent doc belong to one catogory
        for filename in filenames:#输出文件信息
            totaldoc+=1
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

def improvechi(topicwords,cata,totalcw,catagory):  
    print("handle doc begin")        
    i=cata
    cw=totalcw[i]
    m=len(cw)
    dic = dict()
    for j in range(m):
        w=cw[j]
        for k in range(len(w)):
            word=w[k]
            if word in dic:
                continue
            (A,B,re)=chi(word,i,totalcw)
            dic[word]=re
            beta=accuracy(catagory,A,B)
            alpha=frequency(word,w)
            dic[word]=re*beta*alpha
    re=sorted(dic,key=dic.get,reverse=True)
    a=0
    for c in range(len(re)):
        a+=1
        if a>topicwords:#every topic treat topwords as its fature
            break
        wordset.add(re[c])
    print("one catogory end")
    path="F:/python/vocab/"
    path += str(cata)+".txt";
    create_txt(path, wordset)

def combinefile():
    rootdir = "F:/python/vocab/"
    dir = os.walk(rootdir)    
    finalpath="F:/python/vocab.txt"
    word=[]
    for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:#输出文件信息
            path_name=os.path.join(parent,filename)
            file_object = codecs.open(path_name,'r','utf-8')
            try:
                all_the_text = file_object.read()
            finally:
                file_object.close()
            arr=all_the_text.split()
            for i in range(len(arr)):
                word.append(arr[i])
    create_txt(finalpath, word)
    if os.path.exists(rootdir):
        os.remove(rootdir)
    
            
            

    
            
            
            
        
        
        
        
                
                
                
                
            
        
            
        
    