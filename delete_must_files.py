#-*- coding:utf-8 –*-
'''
Created on 2017年12月16日
功能:删除某些必须删除的文件和文件夹
@author: chuangyejia
'''


import shutil

import sys

import os

my_path=sys.path[0]+'/zip/temp'

if len(sys.argv)==2:
    my_path=sys.argv[1]+'/zip/temp'






#获取当前目录下所有文件，返回文件数组，循环获取,包括文件夹
def getAllFilesWithoutDirs(rootDir):
    returnAllFiles=[]
    if   not os.path.isdir(rootDir):
        return returnAllFiles
    for dir_var in os.listdir(rootDir):
        sub_path=os.path.join(rootDir,dir_var)
        if os.path.isdir(sub_path):
            returnAllFiles=returnAllFiles+getAllFilesWithoutDirs(sub_path)
        returnAllFiles.append(sub_path)   
    return returnAllFiles

def delete_file_dir(file_dir):
    if file_dir.find('JSDownloadViewDemo')>=0:
        print '为啥:'+file_dir
    
    if not (os.path.isfile(file_dir) or os.path.exists(file_dir)):
        return 0
    file_name=file_dir.split('/')[-1]
    if os.path.isfile(file_dir) and file_name.find('.')==0:
        os.remove(file_dir)
        return 0
    if os.path.isdir(file_dir) and file_name.find('.')==0:
        shutil.rmtree(file_dir)
        return 0
    #分割文件名称
    
    #删除xcodeproj
    if file_name.find('xcodeproj')>=0 and os.path.isdir(file_dir):
        shutil.rmtree(file_dir)
        return 0
    if file_name.find('AppDelegate')>=0:
        os.remove(file_dir)
        return 0
    #Info.plist
    if file_name.find('nfo.plist')>=0:
        os.remove(file_dir)
        return 0
    #main.m
    if file_name.find('main.m')>=0:
        os.remove(file_dir)
        return 0
    if file_name=='ViewController.h':
        os.remove(file_dir)
        return 0
    if file_name=='ViewController.m':
        os.remove(file_dir)
        return 0
    if file_name=='AppDelegate.h':
        os.remove(file_dir)
        return 0
    if file_name=='AppDelegate.m':
        os.remove(file_dir)
        return 0
    if file_name=='LaunchScreen.storyboard':
        os.remove(file_dir)
        return 0
    if file_name=='Main.storyboard':
        os.remove(file_dir)
        return 0
    #ViewController.swift
    if file_name=='ViewController.swift':
        os.remove(file_dir)
        return 0
#     #删除
    if file_name.find('Tests')>=0 and os.path.isdir(file_dir):
        shutil.rmtree(file_dir)  
        return 0
    if file_name.find('git')>=0 and os.path.isdir(file_dir):
        shutil.rmtree(file_dir)  
        return 0
    if file_name.find('xcassets')>=0 and os.path.isdir(file_dir):
        shutil.rmtree(file_dir)
        return 0
    if file_name.find('DS_Store')>=0 and os.path.isdir(file_dir):
        shutil.rmtree(file_dir)
        return 0 
    if file_name.find('Base.lpro')>=0 and os.path.isdir(file_dir):
        shutil.rmtree(file_dir)
        return 0
    if file_name=='Pods' and os.path.isdir(file_dir):
        shutil.rmtree(file_dir)
        return 0    
    print '未删除:'+file_dir 
    #不需要删除
    return 1
        
    
    
    



a=1
shutil.rmtree(my_path+'/__MACOSX')

for root_dir in os.listdir(my_path):
    a=a+1
    all_file_dirs=[]
    all_file_dirs=getAllFilesWithoutDirs(my_path+'/'+root_dir)
    for file_dir in all_file_dirs:
        if int(delete_file_dir(file_dir))==0:
            print '删除成功:'+file_dir
print '已经删除了'+str(a)










