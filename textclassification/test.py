# -*- coding: UTF-8 -*-
import urllib.request
import os
import shutil
import re
import codecs
import json
from bs4 import BeautifulSoup
import _thread
import jieba
import os
import codecs
import re
import shutil
import jieba.posseg
# html = None
# try:
    # headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    # req = urllib.request.Request(url="http://3g.163.com/touch/article/list/BA8D4A3Rwangning/0-1000.html", headers=headers)
    # html = urllib.request.urlopen(req).read().decode(encoding = 'utf-8', errors='ignore')
# except Exception as e:
    # print(e, "please check your network situation")
# html = html[html.index('(')+1:html.rfind(')')]

# info = json.loads(html)
# url = info["BA8D4A3Rwangning"][1]["url"]
# print(url)
# dic=dict()
# dic['2',1]=3
# dic[4]=5
# if 1 in dic:
    # print("2 in dic")
# if 5 in dic:
    # print("5 in dic")
# s=[]
# for i in range(4):
    # s.append(set())
# s[0].add(2)
# print(s)
rootdir = "F:/1.txt"
s = os.path.getsize(rootdir)
print(s)
# dir = os.walk(rootdir)
# for parent,dirnames,filenames in dir:
   
