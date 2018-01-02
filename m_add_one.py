#-*- coding:utf-8 –*-
#处理.h文件
import random
import string
import re
import sys
import os
if len(sys.argv)<1:
    print '你的工程路径呢?'
    sys.exit()
file_name =sys.argv[1]
# file_name='/Users/chuangyejia/Desktop/工作/aa/KXHomeViewController.m'  


def get_one_method(type_arr):
    m_str='-(void)'
    i=0
    max_parameter=random.randint(5,20)
    while i< max_parameter:
        randomString= 'a'+''.join(random.sample(string.ascii_letters + string.digits, random.randint(4,10)))
        m_type=str(type_arr[random.randint(0,len(type_arr)-1)]).replace("\n", "").replace(' ','')
        if m_type=='':
            continue
        m_str+=randomString+':('+m_type+') '+randomString+' '
        i=i+1
    m_str+='{\n'
    i=0
    max_parameter=random.randint(10,20)
    while i< max_parameter:
        randomString= ''.join(random.sample(string.ascii_letters + string.digits, random.randint(10,40)))
        m_str+='NSLog(@"'+randomString+'");\n'
        i=i+1
    m_str+='}\n'
    return m_str; 




file_object = open(file_name)
file_object_h=open(file_name.replace('.m','.h'))



try:
    all_the_text =str(file_object.read( ))
    all_the_text_h=str(file_object_h.read())
    if  ('@end' in all_the_text) and ('@implementation' in all_the_text) and (('BaseViewController.h' in all_the_text_h) or ('#import <UIKit/UIKit.h>' in all_the_text_h)) :
        #print all_the_text;
        m_file_name=open(sys.path[0]+'/m_file_name.txt')
        try: 
            m_arr=[]
            for line in m_file_name:
                m_arr.append(line)
            all_method_sum=random.randint(3,10);
            all_method=''
            i=0
            while(i<all_method_sum):
                all_method+=get_one_method(m_arr)
                i=i+1
            replace_reg = re.compile(r'@end(\r|\n|\\s)*$')
            all_the_text=replace_reg.sub(all_method,all_the_text)
            file_object.close()
            file_object = open(file_name,'w')
            try:
                file_object.write(all_the_text)
                file_object.write("@end")
                print 'succ :'+file_name
            finally:
                file_object.close()
        finally:
            m_file_name.close()
finally:
    file_object.close( )
