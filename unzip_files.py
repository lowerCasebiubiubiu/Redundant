#-*- coding:utf-8 –*-

'''
Created on 2017年12月16日
功能:  解压多个zip

参数:1:设置解压路径， 

说明:1.解压该路径下的zip文件夹下的所有zip，并放置到zip目录下的temp文件夹下



@author: chuangyejia
'''
import os

import zipfile

import sys
my_path=sys.path[0]+'/zip'

if len(sys.argv)==2:
    my_path=sys.argv[1]+'/zip'


#查找文件夹下所有zip文件
zip_list=[]
for file_name in os.listdir(my_path):
    if(file_name[-3:]=='zip'):
        zip_list.append(my_path+'/'+file_name)
print zip_list

for zip_file_path in zip_list:
    print 'now run:'+zip_file_path
    try:
        f = zipfile.ZipFile(zip_file_path,'r')
        for afile in f.namelist():
            f.extract(afile, my_path+'/temp/')
    except BaseException:
        print "Error:"+zip_file_path
    else:
        print 'succ :'+zip_file_path
    f.close()
    
    

        



