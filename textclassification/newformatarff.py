# -*- coding: UTF-8 -*-
import os
import codecs

def formatonecate(theta):
    
    m=len(theta)
    n=len(theta[0])
    trainpath="F:\\model.arff"
    if os.path.exists(trainpath):
        os.remove(trainpath)      
    train_file=codecs.open(trainpath,'w','utf-8')
    try:
        train_file.write("@relation topic\n")
        for i in range(n):
            train_file.write("@attribute "+str(i+1)+" real\n")
        train_file.write('@ATTRIBUTE class {')
        for i in range(n-1):
            train_file.write(str(i+1)+",")
        train_file.write(str(n)+"}\n")
        train_file.write("@data\n")
        for i in range(m):
            for j in range(n):
                train_file.write(theta[i][j]+',')
            maxvalue=max(theta[i])
            maxindex=theta[i].index(maxvalue)
            train_file.write(str(maxindex+1))
            train_file.write('\n')
    finally:
        train_file.close()


thetapath="F:/Android/JGibbLDA-v.1.0/models/casestudy-en/model-final.theta"
theta_file = codecs.open(thetapath,'r','utf-8')
theta=[]
wordlen=0
try:
    for line in theta_file:
        arr=line.split()
        theta.append(arr)
    formatonecate(theta)     
finally:
    theta_file.close()