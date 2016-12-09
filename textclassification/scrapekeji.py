# -*- coding: utf-8 -*-
# -*- coding:utf-8 -*-
import urllib.request
import os
import shutil
import re
import codecs
import json
from bs4 import BeautifulSoup
import _thread

# import sys   
# sys.setrecursionlimit(1000000)  

def get_url(year,month,day):
    if month<10:
        strmonth = "0"+str(month)
    else:
        strmonth = str(month)
        
    if day<10:
        strday = "0"+str(day)
    else:
        strday = str(day)
    
    url = "http://tech.qq.com/l/"+str(year)+strmonth+"/scroll_"+strday+".htm"
    return url

def get_filelink(url,code):#获取解编码后的HTML
    print(url)
    soup = get_html_soup(url, code)
    if soup == None:
        print("soup none")
        return None
    article_div = str(soup.find("div", attrs = {"class": "mod newslist"}))
    scroll_list = BeautifulSoup(str(article_div), "lxml")
    class_link={}
    for link in scroll_list.find_all("a"):
        class_link[link.get_text()] = link.get('href')
    return class_link
        
def get_html_soup(url,code):#获取解编码后的HTML
    html = None
    try:
        headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
        req = urllib.request.Request(url=url, headers=headers)
        html = urllib.request.urlopen(req).read().decode(encoding = code, errors='ignore')
    except Exception as e:
        print(e, "please check your network situation")
        return None
    soup = BeautifulSoup(str(html), "lxml")   
    return soup
    
def get_news_body(url):#抓取新闻主体内容
    content_text = []
    article_div = ""

    soup = get_html_soup(url, 'gbk')
    if soup == None:
        return None
    article_div = str(soup.find("div", attrs = {"id" : "Cnt-Main-Article-QQ"}))
    # article_div1 = str(soup.find("div", attrs = {"id":"ArticleCnt"}))
    soup = BeautifulSoup(str(article_div), "lxml")
    para_arr = soup.find_all("p")
    lenth = len(para_arr)
    if lenth == 0:
        print("lenth is zero")
        # soup = BeautifulSoup(str(article_div1), "lxml")
        # para_arr = soup.find_all("p")
        # lenth = len(para_arr)
    for i in range(0,lenth - 1):
        if len(para_arr[i].get_text().strip()) > 0:
            content_text.append("    " + para_arr[i].get_text().strip())
    for x in content_text:
        if x == "    None":
            return None
    return content_text

def create_txt(rootdir, title, content):   
    filepath = rootdir + '/'+clean_chinese_character(title) + ".txt"
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
            print("create succeed")

def clean_chinese_character(text):
    '''处理特殊的中文符号,将其全部替换为'-' 否则在保存时Windows无法将有的中文符号作为路径'''
    chars = chars = ['\t'," ","\n","/", "\"", "'", "·", "。","？", "！", "，", "、", "；", ":", "‘", "’", "“", "”", "（", "）", "…", "–", "．", "《", "》","|","?",",","<",">"];
    new_text = ""
    for i in range(len(text)):
        if text[i] not in chars:
            new_text += text[i]
        else:
            if not text[i]==" ":
                new_text += "_"
    return new_text;


minyear = 2010
maxyear = 2016
for m in range(6,13):
    for d in range(1,31):
        url = get_url(2010,m,d)
        classlink = get_filelink(url, 'gbk')
        if classlink == None:
            continue
        for x in classlink:
            class_url=classlink[x]
            content = get_news_body(class_url)
            create_txt("F:/keji",x,content)
for y in range(2011, maxyear):
    for m in range(1,13):
        for d in range(1,31):
            url = get_url(y,m,d)
            classlink = get_filelink(url, 'gbk')
            if classlink == None:
                continue
            for x in classlink:
                class_url=classlink[x]
                content = get_news_body(class_url)
                create_txt("F:/keji",x,content)
                
            

    
    
    
    
    
    
    
    
    
    
    
    
    