# -*- coding: UTF-8 -*-
import threading  
import time
from selectfeature import *

endthreadnum=0
class MyThread(threading.Thread): 

    def __init__(self, topicwords1,cata1,totalcw1,catagory):  
        threading.Thread.__init__(self)
        self.topicwords = topicwords1
        self.cata = cata1
        self.totalcw = totalcw1
        self.catagory = catagory

    def run(self): 
        for i in range(self.cata, self.cata+10):
            improvechi(self.topicwords,i,self.totalcw,self.catagory)
            endthreadnum += 1
        
         
 
if __name__ == "__main__":
    totalcata = 20
    topicwords = 300
    totalcw = getcw(totalcata)
    for i in range(totalcata):
        thread = MyThread(topicwords, i, totalcw,totalcata)  
        thread.start()
        i=i+10
 
    while(True):
        time.sleep(1)
        if endthreadnum == totalcata:
            break
    
    combinefile()
    print("all ends")
    
# endthreadnum=0
# class MyThread(threading.Thread): 

    # def __init__(self, topicwords1, start1, count1, totalcw1,catagory):  
        # threading.Thread.__init__(self)
        # self.topicwords = topicwords1
        # self.start = start1
        # self.count = count1
        # self.totalcw = totalcw1
        # self.catagory = catagory

    # def run(self): 
        # for i in range(start, start+count):
            # improvechi(self.topicwords,i,self.totalcw,self.catagory)
            # endthreadnum += 1
               
 
# if __name__ == "__main__":
    # totalcata = 20
    # topicwords = 300
    # totalcw = getcw(totalcata)
    # distances = 4
    # for i in range(totalcata):
        # thread = MyThread(topicwords, i, distances, totalcw, totalcata)  
        # thread.start()
        # i=i+distances
 
    # while(True):
        # time.sleep(3)
        # if endthreadnum == totalcata:
            # break
    
    # combinefile()
    # print("all ends")
