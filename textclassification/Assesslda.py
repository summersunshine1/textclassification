# -*- coding: UTF-8 -*-
import os
import codecs
import numpy as np
import math

def getvocab():
    vocabpath="F:/model/datatrainvocab.txt"
    vocabfile=codecs.open(vocabpath,'r','utf-8')
    vocab = []
    try:
        all_the_text=vocabfile.read()
        vocab=all_the_text.split()
    finally:
        vocabfile.close()
    print("vocab:")
    print(len(vocab))
    return vocab

def getthetaphi():
    phipath="F:/model/model-final.phi"
    phi_file = codecs.open(phipath,'r','utf-8')
    phi=[]
    try:
        for line in phi_file:
            arr=line.split()
            phi.append(arr)      
    finally:
        phi_file.close()
        
    thetapath="F:/model/model-final.theta"
    theta_file = codecs.open(thetapath,'r','utf-8')
    theta=[]
    try:
        for line in theta_file:
            arr=line.split()
            theta.append(arr)      
    finally:
        theta_file.close()
    m = len(theta)
    n = len(phi)
    for i in range(m):
        theta[i] = list(map(float, theta[i]))
    for j in range(n):
        phi[j] = list(map(float, phi[j]))
    
    newphi = np.transpose(phi)
    print("phi:")
    print(len(newphi))
    return theta,newphi

def getdocword(theta,newphi,docindex,wordindex):
    # print(docindex)
    # print(wordindex)
    docword = np.dot(theta[docindex], newphi[wordindex])
    return docword
    # for i in range(m):
        # docword.append([0]*v)
        # doctopic = theta[i]
        # doctopicnum = len(doctopic)
        # for j in range(v): 
            # topicword = newphi[j]
            # topicwordnum = len(topicword)
            # for x in range(doctopicnum):
                # for y in range(topicwordnum):
                    # docword[i][j] = doctopic[x]*topicword[y]  
    # chunknum1 = 0
    # chunknum2 = 0
    # if m%2==0:
        # chunknum1 = 4
    # else:
        # chunknum1 = 3
    # if v%2 == 0:
        # chunknum2 = 4
    # else: 
        # chunknum2 = 3
    # for i in range(0,m,chunknum1):
        # docword.append([0]*v)
        # for j in range(0,n,chunknum2):
            # docword[i:i+chunknum1] = np.dot(theta[i], newphi[j])
    # for r in range(0, m, SPLITROWS):
        # for c in range(0, numrows, SPLITROWS):
            # r1 = r + SPLITROWS
            # c1 = c + SPLITROWS
            # chunk1 = theta[r:r1]
            # chunk2 = [p[c:c1] for p in phi]

        # docword[r:r1, c:c1] = np.dot(chunk1, chunk2)
    # docword = np.dot(theta, phi)
    # pw = re.sum(axis = 0)
    
def gettotalword():
    handlefile = codecs.open("F:/model/datatrainhandle.txt",'r','utf-8')
    totalword = -1
    # totaldoc=-1
    docs = []
    try:
        for line in handlefile:
            arr=line.split()
            if not totalword==-1:
                docs.append(arr)
            totalword += len(arr)
            # totaldoc +=1            
    finally:
        handlefile.close()
    return totalword,docs

# def getonelinedoc(docindex):
    # handlefile = codecs.open("F:/model/souhuhandle.txt",'r','utf-8')
    # lines = handlefile.readlines()
    # try:
        # line = lines[docindex]
        # arr=line.split()          
    # finally:
        # handlefile.close()
    # return arr
   
def computeperplexity(theta,phi,totalword,docs,vocab):
    m =len(docs)
    re = 0
    for i in range(m):
        doc = docs[i]
        n = len(doc)
        temp = 0
        for j in range(n):
            word = doc[j]
            if not word in vocab:
                print("word not in vocab")
                continue
            wordindex = vocab.index(word)
            # print(wordindex)
            tempdocword = getdocword(theta,phi,i,wordindex)
            # print(tempdocword)
            temp += math.log(tempdocword)
        re += temp
    result = math.exp(-re/totalword)
    return result

topics = [20,50,80,100,150]
# topics = [200]
beta = 0.1
cmd = "java -jar jgibbs.jar -alpha "
minperplexity = 100000000
finaltopic = 0
(totalword,docs) = gettotalword()
result=[]
for i in range(len(topics)):
    topic = topics[i]
    alpha = 50/topic
    cmd+=str(alpha)
    cmd+=" -beta "
    cmd+=str(beta)
    cmd+=" -ntopics "
    cmd+=str(topic)
    cmd+=" -niters 1000 -savestep 100 -twords 10 -dir \"F:/model\" -dfile \"datatrainhandle.txt\" -model"+" model-final"+str(i)
    os.system(cmd)
    (theta,phi)=getthetaphi()
    vocab = getvocab()
    p = computeperplexity(theta,phi,totalword,docs,vocab)
    if p<minperplexity:
        minperplexity = p
        finaltopic = topics[i]
    # print("topics : "+str(topics[i])+" p : "+str(p))
    result.append(p)
for i in range(len(result)):
    print("topic:"+str(topics[i])+" perplexity: " +str(result[i]))
print("min topic is："+ str(finaltopic) + "perplexity is : "+str(minperplexity))

    
    

# java -jar jgibbs.jar -alpha 2.5 -beta 0.1 -ntopics 20 -niters 1000 -savestep 100 -twords 10 -dir "F:/model" -dfile "souhuhandle.txt"



    
        
    


                                                     