# -*- coding: UTF-8 -*-
import codecs

def gettotalword():
    wordset = set()
    handlefile = codecs.open("F:/model/souhuhandle.txt",'r','utf-8')
    totalword = -1
    # totaldoc=-1
    docs = []
    try:
        for line in handlefile:
            arr=line.split()
            if not totalword==-1:
                l = len(arr)
                for i in range(len(arr)):
                    wordset.add(arr[i])
                
            totalword += len(arr)
                         
    finally:
        handlefile.close()
    print(len(wordset))
gettotalword()