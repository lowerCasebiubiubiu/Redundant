#!/bin/bash
basepath=$(cd `dirname $0`; pwd)
python $basepath/reptile_cocochina.py $1 $2 $basepath
echo '***************下载完成**********************'
python $basepath/unzip_files.py $basepath
echo '***************解压完成**********************'
python $basepath/delete_must_files.py $basepath
echo '***************处理完成**********************'



