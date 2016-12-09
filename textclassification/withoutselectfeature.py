# -*- coding: UTF-8 -*-
import os
import codecs
rootdir = "F:/souhutrain"
dir = os.walk(rootdir)
w=[]
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:       #输出文件信息
        path_name=os.path.join(parent,filename)
        file_object = codecs.open(path_name,'r','utf-8')
        try:
            all_the_text = file_object.read()
        finally:
            file_object.close()
        arr=all_the_text.split()
        if not len(arr)==0:
            w.append(arr)
m=len(w)
outputpath="F:/python/souhuhandlewithout.txt"
file_object = codecs.open(outputpath,'w','utf-8')
try:
    file_object.write(str(m)+'\n')
    for i in range(m):
        n=len(w[i])
        for j in range(n):
            file_object.write(w[i][j]+' ')
        if not n==0 and not i==m-1:
            file_object.write('\n')
finally:
    file_object.close()
        