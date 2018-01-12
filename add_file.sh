#!/bin/bash
now_time=`date +%Y_%m_%d_%H_%M_%S`
basepath=$(cd `dirname $0`; pwd)
h_change=`echo $basepath'/log/add_h_'$now_time'.log'`
m_change=`echo $basepath'/log/add_m_'$now_time'.log'`
#echo $h_change

echo ''>$h_change
echo ''>$m_change
hfiles=`find $1 -name "*.h"`
mfiles=`find $1 -name "*.m"`
let 'hsum=0'
let 'msum=0'
for hfile in $hfiles
do

  echo "hfile:"$hfile
hsucc=`python  $basepath/h_add_one.py $hfile`
  echo $hsucc
  echo $hsucc>>$h_change
  let 'hsum++'
done
for mfile in $mfiles
do

  if [[ $mfile =~ 'main.m' ]]
  then
    echo '这是main.m'
    continue
  fi
  echo "mfile:"$mfile
  msucc=`python  $basepath/m_add_one.py $mfile`
  echo $msucc
  echo $msucc>>$m_change
  let 'msum++'
done
python  $basepath/move_files.py $1 $2 $3
echo 'h文件写入日志:'$basepath'/'$h_change
echo 'h文件更新总数:'$hsum
echo 'm文件写入日志:'$basepath'/'$m_change
echo 'm文件更新总数:'$msum

