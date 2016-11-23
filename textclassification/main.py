import os
import codecs


def writeFile(arr,file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    m=len(arr)
    for i in range(m):
        subarr=arr[i]
        lsub=len(subarr)
        for j in range(lsub):
            f.write(str(arr[i][j]))
            if not j==lsub-1:
                f.write(' ')
        if not i==m-1:
            f.write('\n')
    f.close()

    
# doc word
# rootdir = "F:\\doc"
# for test
rootdir="F:/dataset"
w=[]
dir = os.walk(rootdir)
print("word:")
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:                        #输出文件信息
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
        w.append(tempw)
# file_object = codecs.open("F:/train/#断货王#双十一买什么 保险又好用的囤货指南在此new.txt",'r','utf-8')
# try:
    # all_the_text = file_object.read()
    # arr=all_the_text.split()
    # tempw=[]
    # for wa in arr:
        # tempw.append(wa)
    # w.append(tempw)
# finally:
    # file_object.close()
#vocab
v=[]
print("vocab:")     
vocabpath="F:\\python\\vocab.txt"
file_object = codecs.open(vocabpath,'r','utf-8')
try:
    all_the_text = file_object.read()
finally:
    file_object.close()
arr=all_the_text.split()
for wa in arr:
    v.append(wa)

k=25
alpha=2
beta=0.1
maxiter=1000
epsino=0
theta=[]
fi=[]
v1=len(v)
print(v1)
m=len(w)
print(m)
for i in range(m):
    theta.append([0]*k)
for i in range(k):
    fi.append([0]*v1)

print('gibbs')
from gibbs import *
import sys
sys.path.append('F:/python')
(theta,fi)=gibbssample(w,alpha,beta,k,v,maxiter,epsino)

# write fi,theta to txt
file_path='F:/python/fi.txt'
writeFile(fi,file_path)
file_path='F:/python/theta.txt'
writeFile(theta,file_path)

# for test data
# file_path='F:/python/testfi.txt'
# writeFile(fi,file_path)
# file_path='F:/python/testtheta.txt'
# writeFile(theta,file_path)


