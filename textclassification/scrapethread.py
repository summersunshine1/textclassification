# -*- coding:utf-8 -*-
import threading,time
from time import sleep, ctime
from scrapesouhu import *

threadpool=[]
for i in range(13):
    th = threading.Thread(target=scrape, args =(i+1))
    threadpool.append(th)

for th in threadpool:
    th.start()

for th in threadpool :
    threading.Thread.join( th )