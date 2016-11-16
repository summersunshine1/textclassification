# -*- coding: UTF-8 -*-
#divide doc into train doc and test doc
import shutil
import os
rootdir = "F:/doc"
dst = "F:/train"

dir = os.walk(rootdir)
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    i=0
    for filename in filenames:
        if i%2==0:
            path_name=os.path.join(parent,filename)
            dest_path=os.path.join(dst,filename)
            if os.path.exists(dest_path):
                os.remove(dest_path)
            shutil.move(path_name,dst)
        i+=1