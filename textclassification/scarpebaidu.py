# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 21:24:27 2016
 
@author: Administrator
"""
 
import re
import time
import requests
import numpy as np
import os

from bs4 import BeautifulSoup
from collections import Counter
import codecs

 
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"}
 
# 获取首页数据head_data
def get_head_data():
    head_url = 'http://internet.baidu.com/'
    data = requests.get(head_url,headers=headers)
    data.encoding = 'gbk'
    # print(data.status_code)
    head_data = data.text
    return head_data
 
# 获取各新闻分类的title及href
def get_class(head_data):
    title_href = {}
    pa = re.compile(r'<a href="(http.*?.com/).*?>.*?(\w+)</a></li>')
    ma = re.findall(pa,head_data)[1:-7]
    ma = list(set(ma))[:-1]
    # print(len(ma))
    for i in range(len(ma)):
        key = ma[i][1]
        value = ma[i][0]
        title_href[key] = value
    # print(title_href)
    return title_href
 
# 对于每个分类提取标题信息class_data
def get_class_data(class_url):
 
    class_data = requests.get(class_url, headers=headers)
    pa = re.compile(r'charset=(.*?)">')
    charset = re.findall(pa,class_data.text)[0]
    class_data.encoding  = charset
    # class_data.encoding = 'gbk'
    class_data =class_data.text
    soup = BeautifulSoup(class_data, 'lxml')
    data = soup.findAll('a',{'target':'_blank'})
    class_data = {}
    for i in range(len(data)):
        title = data[i].get_text()
        href = data[i].get('href')
        if len(title) > 10:
            if not '下载' in title:
                class_data[title] = href
    return class_data
 
# 获取每条新闻的具体文本内容，粗略抓取
def get_news_text(href):
    try:
        data = requests.get(href,headers=headers)
        # data.encoding = 'gbk'
        pa = re.compile(r'charset=(.*?)">')
        charset = re.findall(pa,data.text)[0]
        data.encoding  = charset
        data = BeautifulSoup(data.text,'lxml').get_text()
        text = re.sub("[A-Za-z0-9\[\`\~\!\@\#\$\ \^\"\-\+\_\\&\\n\\t\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%]", "", data)
    except:
        # print('get New Text fail...')
        text = None
        pass
    return text
    
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
 
 
head_data = get_head_data()
title_href = get_class(head_data)
count = 0
rootdir = "F:/baidu"
for class_title,class_href in dict(title_href).items():
    print(class_title)
    # try:
    class_data = get_class_data(class_href)
    # except:
    #     print('get Class data fail...')
    #     pass
    for news_title, news_url in class_data.items():
        # print(news_title)
        text = get_news_text(news_url)
        create_txt(rootdir,class_title,news_title,text)
        
 
end = time.time()
total_time = end - start
 
T1 = '本次抓取耗时%s'%str(total_time)
T2 = '  &   本次共抓取%s条新闻'%str(count)
T = T1+T2
