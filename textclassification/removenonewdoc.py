import os
import codecs
import shutil
rootdir = "F:/datatest"
dir = os.walk(rootdir)    
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:#输出文件信息
        path_name=os.path.join(parent,filename)          
        if path_name.rfind('new')==-1:
            os.remove(path_name)
        if os.path.getsize(path_name) == 0:
            os.remove(path_name)
            
rootdir = "F:/datarain"
dir = os.walk(rootdir)    
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:#输出文件信息
        path_name=os.path.join(parent,filename)          
        if path_name.rfind('new')==-1:
            os.remove(path_name)
        if os.path.getsize(path_name) == 0:
            os.remove(path_name)
            