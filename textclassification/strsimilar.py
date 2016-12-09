# -*- coding: UTF-8 -*-
import os


def strsimilar(str1, str2):
    if len(str1)==0:
        return len(str2)
    if len(str2)==0:
        return len(str1)
    m=len(str1)
    n=len(str2)
    matrix = []
    for i in range(m+1):
        matrix.append([0]*(n+1))
    for i in range(m+1):
        matrix[i][0]=i
    for i in range(n+1):
        matrix[0][i]=i
    for i in range(1,m+1):
        for j in range(1,n+1):
            matrix[i][j]=max(matrix[i-1][j-1]+1,matrix[i][j-1]+1,matrix[i-1][j]+1)
    dis = matrix[m][n]
    similar = 1-dis/max(len(str1),len(str2))
    return similar
 
def clean_character(text):
    l = len(text)
    newtext=""
    character=['_',"："]
    for i in range(l):
        if text[i] in character:
            newtext+='1'
        else:
            newtext+=text[i]
    return newtext
       
def similar(str1,str2):
    sim = 0
    str1 = clean_character(str1)
    str2 = clean_character(str2)
    if str1 == str2:
        sim=1
    
    return sim


rootdir = "F:\\souhut"
dir = os.walk(rootdir)
count =0 
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    path = []
    deletefile = set()
    for filename in filenames:       #输出文件信息
        # path_name=os.path.join(parent,filename)
        path.append(filename)
        # print(filename)
    l = len(path)
    for i in range(0,l-1):       
        sim= similar(path[i],path[i+1])
        if sim == 1:
            deletefile.add(path[i+1])
    for path_name in deletefile:
        file = os.path.join(parent,path_name)
        if os.path.exists(file):
            os.remove(file)
    print(str(count)+" cate ends")
    count+=1
    

        
        
    
    
    