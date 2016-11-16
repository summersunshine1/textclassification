# -*- coding: UTF-8 -*-
import jieba
import os
import codecs
import re
import shutil
import jieba.posseg

def isnumorletter(num):
    regex = re.search('[a-zA-Z0-9]',num)
    if regex:
        return True
    else:
        return False

def create_txt(file_path, content):
    if os.path.exists(file_path):
        os.remove(file_path)
    index = file_path.rfind(".")
    new_path=file_path[0 : index]+'new.txt'
    f=codecs.open(new_path,'w','utf-8')
    for x in content:
        f.write(x)
    f.close()

def remove_words(file_path):
    stop = []
    for line in codecs.open("F:\\python\\stop_words_ch.txt",'r','gbk'):  
        stop.append(line)
    
    file_object = codecs.open(file_path,'r','utf-8')
    try:
        all_the_text = file_object.read()
    finally:
        file_object.close()
    segs = jieba.posseg.cut(all_the_text)
    final=''
    for seg in segs:
        tempseg=seg.word
        tempflg=seg.flag
        if tempflg.find('n')==-1:#only handle with noun
            continue
        if isnumorletter(seg.word):
            continue
        tempseg+='\n'
        if tempseg not in stop:
            if not len(final)==0:
                seg.word+=' '
            final+=seg.word
    create_txt(file_path, final)
        

rootdir = "F:\\doc"

dir = os.walk(rootdir)
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:                        #输出文件信息
        path_name=os.path.join(parent,filename)
        if not path_name.rfind('new')==-1:
            os.remove(path_name)
            continue
        remove_words(path_name)