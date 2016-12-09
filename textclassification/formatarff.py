# -*- coding: UTF-8 -*-
import os
import codecs
def formatonecate(theta,category,topics):
    currentcate=0
    catenum=category[currentcate]
    count=0 
    m=len(theta)
    l=len(category)
    # trainpath="F:\\souhumodel150.arff"
    
    trainpath="F:\\datatest100.arff"
    if os.path.exists(trainpath):
        os.remove(trainpath)      
        os.remove(trainpath)      
    train_file=codecs.open(trainpath,'w','utf-8')
    try:
        train_file.write("@relation topic\n")
        for i in range(topics):
            train_file.write("@attribute "+str(i+1)+" real\n")
        train_file.write('@ATTRIBUTE class {')
        for i in range(l-1):
            train_file.write(str(i+1)+",")
        train_file.write(str(l)+"}\n")
        train_file.write("@data\n")
        for i in range(m):
            if count==catenum:
                print(count)
                count=0
                currentcate+=1
                catenum=category[currentcate]
            n=len(theta[i])
            for j in range(n):
                train_file.write(theta[i][j]+',')
            count+=1
            train_file.write(str(currentcate+1))
            train_file.write('\n')
    finally:
        train_file.close()

#first traverse folder to know how many docs in a theme
# rootdir = "F:\\souhutrain"
rootdir = "F:\\datatest"
category=[]
dir = os.walk(rootdir)
total=0
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    cate=0
    for filename in filenames: #输出文件信息
        cate+=1
    if not cate==0:
        category.append(cate)
thetapath="F:/Android/JGibbLDA-v.1.0/models/casestudy-en/datatesthandle.txt.model-final.theta"
theta_file = codecs.open(thetapath,'r','utf-8')
theta=[]
wordlen=0
try:
    for line in theta_file:
        arr=line.split()
        theta.append(arr)
        wordlen=len(arr)       
finally:
    theta_file.close()

formatonecate(theta,category,wordlen)