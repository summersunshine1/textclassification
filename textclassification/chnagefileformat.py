import os
import codecs
import shutil
import jieba

import re

import jieba.posseg

from chardet.universaldetector import UniversalDetector

targetFormat = 'utf-8'
outputDir = 'converted'
detector = UniversalDetector()


def remove_words(file_path,format):
    stop = []
    for line in codecs.open("F:\\python\\stop_words_ch.txt",'r','gbk'):  
        stop.append(line)
    if format == None:
        format = 'gbk'
    file_object = codecs.open(file_path,'r',format)
    try:
        all_the_text = file_object.read()
    except Exception as e:
        print(e)   
        return
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
    
    
    
def get_encoding_type(current_file):
    detector.reset()
    f=codecs.open(current_file,'rb')
    for line in f:
        detector.feed(line)
        if detector.done: break
    f.close()
    detector.close()
    return detector.result['encoding']

def convertFileWithDetection(fileName):
    # print("Converting '" + fileName + "'...")
    format=get_encoding_type(fileName)
    print(format)
    remove_words(fileName, format)

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
            

rootdir = "F:/tiyu/tiyu"
dir = os.walk(rootdir)    
for parent,dirnames,filenames in dir:    #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:#输出文件信息
        path_name=os.path.join(parent,filename) 
        file_object = codecs.open(path_name,'r','utf-8')
        try:
            all_the_text = file_object.read()
        except:
            file_object.close()
            convertFileWithDetection(path_name)
            continue
        finally:
            file_object.close()
        