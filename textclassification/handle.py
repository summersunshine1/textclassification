
import os
import codecs
import shutil
def create_txt(file_path, vocabarr):
    if os.path.exists(file_path):
        os.remove(file_path)
    f=codecs.open(file_path,'w','utf-8')
    for word in vocabarr:
        f.write(word)
        f.write('\n')
    f.close()

def combinefile():
    rootdir = "F:/python/vocab"
    dir = os.walk(rootdir)    
    finalpath="F:/python/vocab.txt"
    word=[]
    for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:#输出文件信息
            path_name=os.path.join(parent,filename)
            file_object = codecs.open(path_name,'r','utf-8')
            try:
                all_the_text = file_object.read()
            finally:
                file_object.close()
            arr=all_the_text.split()
            for i in range(len(arr)):
                word.append(arr[i])
    create_txt(finalpath, word)
    shutil.rmtree(rootdir)
combinefile()