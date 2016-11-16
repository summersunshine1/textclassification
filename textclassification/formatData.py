# -*- coding: UTF-8 -*-
import os
import codecs

def formatonecate(theta,category):
    currentcate=0
    catenum=category[currentcate]
    count=0 
    m=len(theta)
    trainpath="F:\\python\\traindata.txt"
    if os.path.exists(trainpath):
        os.remove(trainpath)      
    train_file=codecs.open(trainpath,'w','utf-8')
    try:
        for i in range(m):
            if count==catenum:
                print(count)
                count=0
                currentcate+=1
                catenum=category[currentcate]
            n=len(theta[i])
            train_file.write(str(currentcate))
            train_file.write(' ')
            for j in range(n):
                train_file.write(str(j+1)+':')
                train_file.write(theta[i][j]+' ')
            count+=1
            if not i==m:
                train_file.write('\n')
    finally:
        train_file.close()
        


#first traverse folder to know how many docs in a theme
rootdir = "F:\\doc"
category=[]
dir = os.walk(rootdir)
total=0
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    cate=0
    for filename in filenames: #输出文件信息
        cate+=1
    if not cate==0:
        category.append(cate)
thetapath="F:\\python\\theta.txt"
theta_file = codecs.open(thetapath,'r','utf-8')
theta=[]
try:
    for line in theta_file:
        arr=line.split()
        theta.append(arr)    
finally:
    theta_file.close()

formatonecate(theta,category)

