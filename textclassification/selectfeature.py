# -*- coding: UTF-8 -*-
import os
import codecs
import math
import shutil
import _thread
import threading,time
from time import sleep, ctime

def getwordset(totalcw):
    m = len(totalcw)
    wordarr=set()
    f = dict()
    for i in range(m):
        n=len(totalcw[i])
        first = 0
        flag = dict()
        for j in range(n):
            l = len(totalcw[i][j])
            for k in range(l):
                word = totalcw[i][j][k]
                wordarr.add(word)
                if word in flag:
                    continue
                flag[word]=1
                if not word in f:
                    f[word]=1
                else:
                    f[word]+=1              
    return wordarr,f
    
# def accuracy(catanum,A,B):
    # beta=dict()
    # for k,v in A.items():
        # beta[k]=math.pow(catanum, A[k]/(A[k]+B[k]))
    # return beta
           
# def frequency(totalcw):
    # wordarr = getwordset(totalcw)
    # m = len(totalcw)
    # alpha=dict()
    # for i in range(m):
        # docs = totalcw[i]
        # for j in range(len(docs)):
            # f=dict()
            # doc = totalcw[i][j]
            # if len(doc)==0:
                # continue
            # for k in range(len(doc)):
                # word=doc[k]
                # if not word in f:
                    # f[word]=1
                # else:
                    # f[word]+=1
            # if not (i,word) in alpha:
                # alpha[(i,word)] = f[word]/len(doc)
            # else:
                # alpha[(i,word)] += f[word]/len(doc)
    # for i in range(m):
        # for word in wordarr:
            # if not (i,word) in alpha:
                # alpha[(i,word)] = 0
    # return alpha

def improvefrequency(totalcw,wordarr):
    m = len(totalcw)
    alpha=dict()
    for i in range(m):
        docs = totalcw[i]
        f=dict()
        totalword = 0
        for j in range(len(docs)):
            doc = totalcw[i][j]
            lenth = len(doc)
            if lenth==0:
                continue
            totalword += lenth
            for k in range(len(doc)):
                word=doc[k]
                if not word in f:
                    f[word]=1
                else:
                    f[word]+=1
        for k in f:
            alpha[(i,k)] = (f[k]+1)/(totalword+m)#lapalace
        
    for i in range(m):
        for word in wordarr:
            if not (i,word) in alpha:
                alpha[(i,word)] = 1/m
    return alpha
   
def improveidf(totalcw,wordarr,f):
    m = len(totalcw)
    idf = dict()
    for word in wordarr:
        # print("word: "+word+" "+str(f[word]))
        idf[word] = math.log(m/(f[word]+1), 2)
    return idf          

def chi(totalcw,wordarr):
    A=dict()
    B=dict()
    re=dict()
    m=len(totalcw)
    wordtype=dict()
    totaldoc=0
    
    for i in range(m):
        n=len(totalcw[i])
        totaldoc+=n
               
    for i in range(m):
        n=len(totalcw[i])
        for j in range(n):
            l = len(totalcw[i][j])
            flag=dict()
            for k in range(l):
                word = totalcw[i][j][k]
                if word in flag:
                    continue
                flag[word] = 1                    
                if not (i,word) in A:
                    A[(i,word)]=1
                else:
                    A[(i,word)]+=1
                if not word in wordtype:
                    wordtype[word]=set()
                wordtype[word].add(i)
        
    # for i in range(m):
        # n=len(totalcw[i])
        # for word in wordarr:
            # if not (i,word) in A:
                # A[(i,word)]=0
            # C[(i,word)] = n-A[(i,word)] 
    
    for word in wordarr:
        typeset=wordtype[word]
        for j in range(m):
            B[(j,word)] = 0
            for k in typeset:
                if not k==j:
                    B[(j,word)]+=A[(k,word)]
                
    # for i in range(m):
        # n=len(totalcw[i])
        # for word in wordarr:
            # if not (i,word) in B:
                # B[(i,word)]=0
            # D[(i,word)] = totaldoc-n-B[(i,word)]
    
    for i in range(m):
        n=len(totalcw[i])
        for word in wordarr:
            if not (i,word) in A:
                A[(i,word)]=0
            if not (i,word) in B:
                B[(i,word)]=0
            key=(i,word)
            # print(str(i)+" "+word + " A :"+str(A[key])+ " B: "+str(B[key])+" C :"+str(C[key])+ " D: "+str(D[key]))
            re[key] = (A[key]*(totaldoc-n-B[key])-B[key]*(n-A[key]))/((A[key]+B[key])*(-A[key]+totaldoc-B[key]))
            # print(re[key])               
    return re
    
def improvechi(topicwords):
    totalcw = getcw()
    # totalcw = [[["lan","zu"],["you","pao"]],[["lan","du"],["kan","yue"],["xi","xian"]],[['ha','lo'],['hei','vhi']]]
    (wordarr,f) = getwordset(totalcw) 
    m = len(totalcw)
    print("begin chi")
    re = chi(totalcw,wordarr)
    print("end chi")
    # beta = accuracy(m,A,B)
    # alpha = frequency(totalcw)
    alpha = improvefrequency(totalcw,wordarr)
    print("end freuency")
    idf = improveidf(totalcw,wordarr,f)
    print("end idf")
    wordset=set()
    # file_path = "F:/python/topic.txt"
    # if os.path.exists(file_path):
        # os.remove(file_path)
    # f=codecs.open(file_path,'w','utf-8')
    
    for i in range(m):
        dic=dict()
        for word in wordarr:
            if not (i,word) in re:
                continue
            key=(i,word)
            # print(str(i)+" "+word + " alpha :"+str(alpha[key])+ " idf: "+str(idf[word])+" re: "+str(re[key]))
            dic[word] = re[key]*alpha[key]*idf[word]
            # print("word: "+word + " "+str(dic[word])
        result=sorted(dic,key=dic.get,reverse=True)
        for j in range(len(result)):
            if j>=topicwords:#every topic treat topwords as its fature
                break
            wordset.add(result[j])
            # f.write(result[j]+'\n')
        # print("one cateends")
    path="F:/python/"
    path += "datatrainvocab.txt";
    create_txt(path, wordset)
        
# def getoncatevocab(cate,topicwords):
    
    
# def frequency(t,w):
    # alpha=0
    # m=len(w)
    # for i in range(m):
        # dic = dict()
        # wordarr=w[i]
        # n=len(wordarr) 
        # for j in range(n):
            # word=wordarr[j]
            # if word==t:
                # if word in dic:
                    # dic[word]+=1
                # else:
                    # dic[word]=1
        # for k,v in dic.items():
            # alpha=alpha+v/n
    # return alpha
        
# def accuracy(M,A,B):
    # beta=math.pow(M,A/(A+B))
    # return beta
    
# def chi(t,c,totalcw):
    # A=0
    # B=0
    # C=0
    # D=0
    # m=len(totalcw)
    # for i in range(m):
        # w=totalcw[i]
        # n=len(w)
        # if i==c:
            # for j in range(n):
                # if t in w[j]:
                    # A+=1
                # else:
                    # C+=1
        # else:
            # for j in range(n):
                # if t in w[j]:
                    # B+=1
                # else:
                    # D+=1       
    
    # re=(A*D-B*C)/((A+B)*(C+D))
    # return A,B,re


        
def create_txt(file_path, vocabarr):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for word in vocabarr:
        f.write(word)
        f.write('\n')
    f.close()
    
def getcw():
    rootdir = "F:/datatrain"
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

# def improvechi(topicwords,cata,totalcw,catagory):  
    # print("handle doc begin")        
    # i=cata
    # cw=totalcw[i]
    # m=len(cw)
    # dic = dict()
    # for j in range(m):
        # w=cw[j]
        # for k in range(len(w)):
            # word=w[k]
            # if word in dic:
                # continue
            # (A,B,re)=chi(word,i,totalcw)
            # dic[word]=re
            # beta=accuracy(catagory,A,B)
            # alpha=frequency(word,w)
            # dic[word]=re*beta*alpha
    # re=sorted(dic,key=dic.get,reverse=True)
    # a=0
    # wordset=set()
    # for c in range(len(re)):
        # a+=1
        # if a>topicwords:#every topic treat topwords as its fature
            # break
        # wordset.add(re[c])
    # print("one catogory end")
    # path="F:/python/vocab/"
    # path += str(cata)+".txt";
    # create_txt(path, wordset)

# def combinefile():
    # rootdir = "F:/python/vocab"
    # dir = os.walk(rootdir)    
    # finalpath="F:/python/vocab.txt"
    # word=[]
    # for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        # for filename in filenames:#输出文件信息
            # path_name=os.path.join(parent,filename)
            # file_object = codecs.open(path_name,'r','utf-8')
            # try:
                # all_the_text = file_object.read()
            # finally:
                # file_object.close()
            # arr=all_the_text.split()
            # for i in range(len(arr)):
                # word.append(arr[i])
    # create_txt(finalpath, word)
    # shutil.rmtree(rootdir)
    
topicwords = 500
improvechi(topicwords)
   
            
            
            
        
        
        
        
                
                
                
                
            
        
            
        
    