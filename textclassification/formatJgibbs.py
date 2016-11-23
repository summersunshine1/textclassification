import os
import codecs

rootdir = "F:/dataset"
dir = os.walk(rootdir)
newfilepath="F:/python/handle1.txt"
cw=[]
vocabpath="F:/python/vocab1.txt"

vocabfile=codecs.open(vocabpath,'r','utf-8')
try:
    all_the_text=vocabfile.read()
    vocab=all_the_text.split()
finally:
    vocabfile.close()

for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:#输出文件信息
        path_name=os.path.join(parent,filename)
        file_object = codecs.open(path_name,'r','utf-8')
        try:
            all_the_text = file_object.read()
        finally:
            file_object.close()
        arr=all_the_text.split()
        tempw=[]
        for wa in arr:
            if wa in vocab:
                tempw.append(wa)
        if len(tempw)==0:
            continue
        cw.append(tempw)

new_file = codecs.open(newfilepath,'w','utf-8')
try:
    n=len(cw)
    new_file.write(str(n)+'\n')
    for i in range(n):
        arr=cw[i]
        m=len(arr)
        for j in range(m):
            new_file.write(arr[j]+' ')
        new_file.write('\n')
finally:
    new_file.close()
    

