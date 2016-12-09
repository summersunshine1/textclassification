# -*- coding:utf-8 -*-
import urllib.request
import os
import shutil
import re
import codecs
import json
from bs4 import BeautifulSoup
import _thread

import sys   
sys.setrecursionlimit(1000000)  

def get_url(pno,partialurl):
    url = "http://3g.163.com/touch/article/list/"+partialurl+"/"+str(pno)+"-1000.html"
    # print(url)
    return url

def get_fileinfo(url,code,partialurl):#获取解编码后的HTML
    html = None
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib.request.Request(url=url, headers=headers)
        html = urllib.request.urlopen(req).read().decode(encoding = code, errors='ignore')
    except Exception as e:
        print(e, "url is "+url)
        return None
    if html == None:
        print("html null")
        return
    html = html[html.index('(')+1:html.rfind(')')]
    info = json.loads(html)
    n = len(info[partialurl])
    print(n)
    path=[]
    title=[]
    for i in range(1,n):
        if not "docid" in info[partialurl][i]:
            continue
        if not "url" in info[partialurl][i]:
            continue
        
        path.append(info[partialurl][i]["url"])
        title.append(info[partialurl][i]["title"])
    return path,title

def get_html_soup(url,code):#获取解编码后的HTML
    html = None
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib.request.Request(url=url, headers=headers)
        html = urllib.request.urlopen(req).read().decode(encoding = code, errors='ignore')
        
    except Exception as e:
        # print(e, "url is"+url)
        return None
    soup = BeautifulSoup(str(html), "lxml")   
    return soup
    
def get_news_body(url):#抓取新闻主体内容
    content_text = []
    article_div = ""

    soup = get_html_soup(url, 'utf-8')
    # print(url)
    if soup == None:
        return None
    article_div = str(soup.find("div", attrs = {"class": "content"}))
    soup = BeautifulSoup(str(article_div), "lxml")
    para_arr = soup.find_all("p")
    lenth = len(para_arr)
    for i in range(0,lenth - 1):
        if len(para_arr[i].get_text().strip()) > 0:
            content_text.append("    " + para_arr[i].get_text().strip())
    for x in content_text:
        if x == "    None":
            return None
    return content_text

def create_txt(rootdir, type, title, content):   
    filepath=rootdir+'/'+type
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    filepath+= '/'+clean_chinese_character(title) + ".txt"
    if os.path.exists(filepath):
        return
    f=None
    try:
        f=codecs.open(filepath,'w','utf-8')
        for x in content:
            f.write(x)
            f.write('\n')
    except Exception as e:
        return None    
    finally:
        if not f==None:
            f.close()
            print("create "+type+" succeed")

def clean_chinese_character(text):
    # '''处理特殊的中文符号,将其全部替换为'-' 否则在保存时Windows无法将有的中文符号作为路径'''
    chars = chars = ['\t'," ","\n","/", "\"", "'", "·", "。","？", "！", "，", "、", "；", ":", "‘", "’", "“", "”", "（", "）", "…", "–", "．", "《", "》","|","?",",","<",">"];
    new_text = ""
    for i in range(len(text)):
        if text[i] not in chars:
            new_text += text[i]
        else:
            if not text[i]==" ":
                new_text += "_"
    return new_text

  
topic=["caijing","yule", "shishang","keji","youxi","qiche","jiaoyu","tiyu"]
partialurl = ["BA8EE5GMwangning","BA10TA81wangning","BA8F6ICNwangning","BA8D4A3Rwangning","BAI6RHDKwangning", "BA8DOPCSwangning","BA8FF5PRwangning","BA8E6OEOwangning"]

def scrape(num):
    totalpsize=300
    rootdir="F:/wangyi"
    for j in range(totalpsize):
        url = get_url(j, partialurl[num])
        (path,title)=get_fileinfo(url,'utf-8',partialurl[num])
        pathnum=len(path)
        for l in range(pathnum):
            if path[l].find("http")==-1:
                newpath="http:"+path[l]
                path[l] = newpath
            content=get_news_body(path[l])
            if content==None:
                continue
            create_txt(rootdir, topic[num], title[l], content)
            
            
import threading,time
from time import sleep, ctime

threadpool=[]
# for i in range(8):
th = _thread.start_new_thread(scrape,(3,))
    # threadpool.append(th)
while(True):
    time.sleep(10)
    print(10)
# for th in threadpool:
    # th.start()

# for th in threadpool :
    # threading.Thread.join( th )



    
    
    
    
    
    
    
    
    
    
    
    
    