# -*- coding: UTF-8 -*-
#divide doc into train doc and test doc
import shutil
import os
rootdir = "F:/datatrain"
dst = "F:/datatest"

dir = os.walk(rootdir)
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    i=0
    if not parent==rootdir:
        index = parent.rfind("\\")
        classfolder = parent[(index+1):]
        newfolder = os.path.join(dst,classfolder)
        if not os.path.exists(newfolder):
            os.mkdir(newfolder)
    for filename in filenames:
        if i%2==0:
            path_name=os.path.join(parent,filename)
            dest_path=os.path.join(newfolder,filename)
            if os.path.exists(dest_path):
                os.remove(dest_path)
            shutil.move(path_name,newfolder)
        i+=1