# -*- coding: UTF-8 -*-
#divide doc into train doc and test doc
import shutil
import os
rootdir = "F:/doc"
dst = "F:/train"

dir = os.walk(rootdir)
for parent,dirnames,filenames in dir:    #�����������ֱ𷵻�1.��Ŀ¼ 2.�����ļ������֣�����·���� 3.�����ļ�����
    i=0
    for filename in filenames:
        if i%2==0:
            path_name=os.path.join(parent,filename)
            dest_path=os.path.join(dst,filename)
            if os.path.exists(dest_path):
                os.remove(dest_path)
            shutil.move(path_name,dst)
        i+=1