#-*- coding:utf-8 –*-
import os

import random

import shutil

import sys

import time

# # 定义填充目录
in_source='/Users/chuangyejia/Desktop/工作/CAISHEN/CAISHEN'
#
# #定义冗余文件夹目录
in_redundant='/Users/chuangyejia/Desktop/aaa'
define_sum=2
#定义文件夹对比数
if len(sys.argv)<4:
    define_sum=2
    if len(sys.argv)<3:
        print '\n至少有两个参数，第一个参数是工程路径，第二个参数是冗余代码路径!!!   请重新执行'
        sys.exit()
    in_source=sys.argv[1]
    in_redundant=sys.argv[2]
else:
    in_source=sys.argv[1]
    in_redundant=sys.argv[2]
    define_sum=sys.argv[3]

#从连续数字中获取不重复数字，个数用sum限制 
def getRandomNumberArray(Nsum,Nmin,Nmax):
    returnNumberArray=[]
    allNumberArray=[]
    currentNumber=0;
    while(currentNumber+Nmin<Nmax):#获取数量
        allNumberArray.append(currentNumber+Nmin)
        currentNumber=currentNumber+1
    i=0
    while i<Nsum:
        i=i+1
        if(len(allNumberArray)<=0):
            break
        randomIndex=random.randint(0, len(allNumberArray)-1)
        returnNumberArray.append(allNumberArray[randomIndex])
        del allNumberArray[randomIndex]
    return returnNumberArray

def getAllDirsWithoutFiles(rootDir):  #排除Images.xcassets 目录
    returnAllDirs=[]
    for dir_var in os.listdir(rootDir):
        sub_path=os.path.join(rootDir,dir_var)
        if os.path.isdir(sub_path) and dir_var!='Images.xcassets' and dir_var!='Base.lproj' and  dir_var!='Assets.xcassets':
            returnAllDirs=returnAllDirs+getAllDirsWithoutFiles(sub_path)
            returnAllDirs.append(sub_path)
    return returnAllDirs


#获取当前目录下所有文件，返回文件数组，循环获取，不获取文件夹
def getAllFilesWithoutDirs(rootDir):
    returnAllFiles=[]
    for dir_var in os.listdir(rootDir):
        sub_path=os.path.join(rootDir,dir_var)
        if os.path.isdir(sub_path):
            returnAllFiles=returnAllFiles+getAllFilesWithoutDirs(sub_path)
        else:
            returnAllFiles.append(sub_path)   
    return returnAllFiles
def move_the_same_dir(path_file,target_path,file_object):
    if(path_file.split('.')[-1]=='m' or path_file.split('.')[-1]=='xib'):
        return
    
    if os.path.isfile(path_file):
        shutil.copyfile(redundant_file, target_path)
        print '移动h文件:'+redundant_file.split('/')[-1]+'        目标路径:'+target_path
        try:
            file_object.write('移动h文件:'+redundant_file+'        目标路径:'+target_path)
        except:
            print '\n复制文件时发生日志写入错误,目录'+log_dir
            sys.exit()
    true_path=target_path[:-1]
    m_path=path_file[:-1]+'m'
    if os.path.isfile(m_path):
        shutil.copyfile(m_path, true_path+'m')
        print '移动m文件:'+m_path.split('/')[-1]+'        目标路径:'+true_path+'m'
        try:
            file_object.write('移动m文件:'+m_path+'        目标路径:'+true_path+'m')
        except:
            print '\n复制文件时发生日志写入错误,目录'+log_dir
            sys.exit()
    xib_path=path_file[:-1]+'xib'
    if os.path.isfile(xib_path):
        shutil.copyfile(xib_path, true_path+'xib')
        print '移动xib文件:'+xib_path.split('/')[-1]+'    目标路径:'+true_path+'xib'
        try:
            file_object.write('移动xib文件:'+m_path+'    目标路径:'+true_path+'xib')
        except:
            print '\n复制文件时发生日志写入错误,目录'+log_dir
            sys.exit()
    return 







#创建log日志文件
log_dir=sys.path[0]+'/'+time.strftime('log/copy_files_%Y_%m_%d_%H_%M_%S.log',time.localtime(time.time()))
file_object = open(log_dir,'w')
#计算填充目录文件夹的路径以及文件夹数目(包括子目录文件夹)，并且保存数组，计做source_dirs
# append
print '\n开始复制文件:'
#print '工程目录:'+in_source
#print '冗余目录:'+in_redundant
#print '工程倍数:'+str(define_sum)
source_dirs=getAllDirsWithoutFiles(in_source)
if len(source_dirs)==0:
    print '\n获取目录列表失败，错误的工程路径'
    sys.exit()
print '\n获取目录列表成功:'+str(source_dirs)
print '\n*************************************************\n'
#计算冗余文件夹的当前目录数目，每个目录单独一个项目，并且每个目录没有互相依赖关系,计做redundant_dirs
redundant_dirs=[]
for dir_var in os.listdir(in_redundant):
    sub_path = os.path.join(in_redundant, dir_var)
    if os.path.isdir(sub_path):#仅仅添加目录
        redundant_dirs.append(sub_path)    
print '\n获取冗余目录列表成功:'+str(redundant_dirs)
print '\n*************************************************'
if len(redundant_dirs)==0:
    print '\n获取冗余目录表失败，错误的冗余代码路径，该目录下无文件夹，请放置多个互不冲突并且独立的文件夹'
    sys.exit()
#随机数量，该数量为填充目录数的2倍，当不足两倍的时候，用总冗余文件夹目录代替，计做random_redundant_dirs_sum
if((define_sum*len(source_dirs))>len(redundant_dirs)):
    random_redundant_dirs_sum=len(redundant_dirs)
else:
    random_redundant_dirs_sum=(define_sum*len(source_dirs))
print '\n将要插入的冗余目录总数目为:'+str(random_redundant_dirs_sum)#获取数量

#获取从random_redundant_files_sum数量的数字，数字从0-redundant_dirs_sum中取得，数量为random_redundant_dirs_sum个，放置到select_redundant_dir_sum数组中
# print getRandomNumberArray(5,1,5)
select_redundant_dir_sum=getRandomNumberArray(random_redundant_dirs_sum,0,len(redundant_dirs))
print select_redundant_dir_sum
#遍历select_redundant_dir_sum数组，获取内容数值，该数值为0-redundant_dirs中的随机一个，不会有重复。
#遍历的时候，通过redundant_dirs数组获取真实冗余目录路径，获取当前路径下的所有文件路径，放置到redundant_files数组中。
#遍历redundant_files数组，每一次遍历获取redundant_file，随机生成数字(数字范围:0-source_dirs之间），利用生成的数字，在source_dirs中寻找实际路径source_dir
#使用redundant_file复制到source_dir中，并且写入文件copy_files.log
for random_index in select_redundant_dir_sum:
    redundant_dir=redundant_dirs[random_index]
    try:
        file_object.write('载入冗余工程:'+redundant_dir)
    except:
        print '\n载入冗余工程时发生日志写入错误,目录'+log_dir
        sys.exit()
try:
    file_object.write('*****载入完成,共复制'+str(len(select_redundant_dir_sum))+'个目录,复制到'+str(len(source_dirs))+'文件夹中，开始复制文件********************')
except:
        print '\n载入完成后发生日志写入错误,目录'+log_dir
        sys.exit()
for random_index in select_redundant_dir_sum:
    redundant_dir=redundant_dirs[random_index]
    print '\n正在复制冗余目录:'+redundant_dir
    redundant_files=getAllFilesWithoutDirs(redundant_dir)
    for redundant_file in redundant_files:
        if redundant_file.split('/')[-1]=='.DS_Store':
            print '跳过复制.DS_Store文件'
            continue
        random_source_dir=source_dirs[random.randint(0,len(source_dirs)-1)]+'/'+redundant_file.split("/")[-1]
        if(redundant_file.split('.')[-1]=='h' or redundant_file.split('.')[-1]=='m' or redundant_file.split('.')[-1]=='xib'):
            move_the_same_dir(redundant_file,random_source_dir,file_object)
            continue
        #移动文件
        shutil.copyfile(redundant_file, random_source_dir)
        print '移动普通文件:'+redundant_file+' 目标目录:'+random_source_dir
        try:
            file_object.write('复制文件:'+redundant_file+'  '+random_source_dir)
        except:
            print '\n复制文件时发生日志写入错误,目录'+log_dir
            sys.exit()
file_object.close()
print '移动文件日志:'+log_dir
print '冗余工程数量:'+str(len(redundant_dirs))




