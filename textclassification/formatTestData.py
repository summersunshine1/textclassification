# -*- coding: UTF-8 -*-
import os
import codecs

def formatonecate(theta):
    m=len(theta)
    trainpath="F:\\python\\test.txt"
    if os.path.exists(trainpath):
        os.remove(trainpath)      
    train_file=codecs.open(trainpath,'w','utf-8')
    try:
        for i in range(m):
            train_file.write(str(1))
            train_file.write(' ')
            n=len(theta[i])
            for j in range(n):
                train_file.write(str(j+1)+':')
                train_file.write(theta[i][j]+' ')
            if not i==m:
                train_file.write('\n')
    finally:
        train_file.close()
        


#first traverse folder to know how many docs in a theme
thetapath="F:\\python\\testtheta.txt"
theta_file = codecs.open(thetapath,'r','utf-8')
theta=[]
try:
    for line in theta_file:
        arr=line.split()
        theta.append(arr)    
finally:
    theta_file.close()

formatonecate(theta)

