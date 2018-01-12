#-*- coding:utf-8 –*-

'''
Created on 2017年12月16日
功能:  从cocochina上下载多个zip，编号从参数获取

参数:1.设置结束号码
    2.设置开始号码
    3:设置本地下载路径 

说明:1.下载量=结束号码-开始号码
    2.zip将会下载到设置的下载路径下的zip文件夹



@author: chuangyejia
'''


import urllib2
import re
import sys
import os



jcy_url='http://code.cocoachina.com'
max_down=100
now_down=0
file_path=sys.path[0]
if len(sys.argv)==3:
    max_down=int(sys.argv[1])
    now_down=int(sys.argv[2])
    print 'aaaaa'
if len(sys.argv)==4:
    max_down=int(sys.argv[1])
    now_down=int(sys.argv[2])
    print file_path
    file_path=sys.argv[3]
    print file_path
    print 'bbbb'



def download_file(from_url,to_path,now_down,max_down):  
    conn = urllib2.urlopen(from_url)
    print '正在下载第'+str(now_down)+'个(总共:'+str(max_down)+'个)，当前下载地址:'+from_url
    f = open(to_path,'wb')  
    print to_path
    f.write(conn.read())  
    f.close()


def get_down_url(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    down_url_text=response.read()
    my_re=re.compile(r'/download/[0-9]*')
    down_url=re.findall(my_re, down_url_text)
    now_down_url=''
    if len(down_url)>0:
        now_down_url=jcy_url+down_url[0]
    print 'succ '+now_down_url
    return now_down_url


file_path=file_path+'/zip'
if(not os.path.exists(file_path)):
    os.makedirs(file_path)
request = urllib2.Request(jcy_url)
response = urllib2.urlopen(request)
text_all=response.read()
myre=re.compile(r'<a\s*href="/[a-zA-Z]*/[0-9]*/[0-9]*">')
arr=re.findall(myre,text_all)

list_root=[]
#查找地址，插入list
for one_root in arr:
    myre=re.compile(r'/[a-zA-Z]*/[0-9]*/[0-9]*') 
    list_root.append(jcy_url+re.findall(myre,one_root)[0])

#对每一个地址进行遍历，插入新的根数组
f_url = open(file_path+'/down_url.txt','wb')  


list_url_product=[]
for one_root in list_root:
    print one_root
    myre0=re.compile(r'[0-9]*$')
    one_url_head=myre0.sub('', one_root)
    print one_url_head
    request1 = urllib2.Request(one_root)
    response1 = urllib2.urlopen(request1)
    text_all=response1.read()
    myre=re.compile(r'<a[^<]+?末页</a>')
    a_all_text=re.findall(myre,text_all)[0]
    myre2=re.compile(r'/[a-zA-Z]*/[0-9]*/[0-9]*')
    url_max_page=re.findall(myre2,a_all_text)[0]
    myre3=re.compile(r'[0-9]*$')
    max_page=re.findall(myre3, url_max_page)[0]
    print max_page
    max_page_int=int(max_page)
    i=0
    while i<=max_page_int:
        i=i+1
        page_url=one_url_head+str(i)
        request2 = urllib2.Request(page_url)
        response2 = urllib2.urlopen(request2)
        text_all=response2.read()
        now_re=re.compile(r'<a\s*href="/[a-zA-Z]*/[0-9]*"\s*target="_blank">')
        one_select_arr=re.findall(now_re,text_all)
        for one_select in one_select_arr:
            myre=re.compile(r'/[a-zA-Z]*/[0-9]*')
            one_select_text=re.findall(myre,one_select)[0]
            one_select_url=jcy_url+one_select_text
            print one_select_url
            down_url=get_down_url(one_select_url)
            if down_url!='':
                list_url_product.append(down_url)
                now_down=now_down+1
                if now_down>max_down:
                    sys.exit()
                f_url.write(down_url+'\n')
                download_file(down_url, file_path+'/'+str(now_down)+'.zip', now_down, max_down)
f_url.close()                


 
 
 
