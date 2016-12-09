# -*- coding: UTF-8 -*-
import codecs
import shutil
import os

def create_txt(file_path, vocabarr):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for word in vocabarr:
        f.write(word)
        f.write('\n')
    f.close()
    
rootdir = "F:\\dataset"
vocab = set()
dir = os.walk(rootdir)
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:       #输出文件信息
        path_name=os.path.join(parent,filename)
        file_object = codecs.open(path_name,'r','utf-8')
        try:
            all_the_text = file_object.read()
        finally:
            file_object.close()
        arr=all_the_text.split()
        # print("len："len(arr))
        for w in arr:
            vocab.add(w)

create_txt("F:\\python\\vocab1.txt", vocab)
        
        