#-*- coding:utf-8 –*-
#处理.h文件
import random
import string
import re
import sys
if len(sys.argv)<1:
    print '你的工程路径呢?'
    sys.exit()
file_name =sys.argv[1]

# file_name='/Users/chuangyejia/Desktop/工作/aa/KXHomeViewController.h'


file_object = open(file_name)
try:
    all_the_text =str(file_object.read())
    if  ('BaseViewController.h' in all_the_text )or(('#import <UIKit/UIKit.h>' in all_the_text)and ('@end' in all_the_text)):
        h_file_name=open(sys.path[0]+'/h_file_name.txt')
        try: 
            i=0
            h_arr=[]
            for line in h_file_name:
                h_arr.append(line)
                i=i+1
            h_select_all_string=''
            i=0
            while(i<random.randint(7,len(h_arr)-1)):
                jcyranint=random.randint(0,len(h_arr)-1)#随机位置
                h_select_one=str(h_arr[jcyranint])#随机位置对应的属性
                #随机生成一个字符串
                randomString= 'a'+''.join(random.sample(string.ascii_letters + string.digits, random.randint(4,10)))   
                h_select_one=h_select_one.replace('jcy',randomString)
                h_select_all_string=h_select_all_string+h_select_one
                i=i+1
            h_select_all_string=h_select_all_string+"@end"
            all_the_text=all_the_text.replace('@end', h_select_all_string)
            file_object.close()
            file_object=open(file_name,'w')
            try:
                file_object.write(all_the_text)
                print 'succ:'+file_name
            finally:
                file_object.close()
        finally:
            h_file_name.close()
#     print all_the_text
finally:
    file_object.close( )
