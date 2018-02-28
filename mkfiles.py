#-*- coding:utf-8 –*-

import urllib
import urllib2
import json
import sys
import os
className='KX'
classCount=30
if len(sys.argv)>1:
    className = sys.argv[1]
if len(sys.argv)>2:
    classCount=sys.argv[2]

url = "http://www.ourname.xin/redundancy/classNames.php?headName="+className+"&count="+str(classCount)

req = urllib2.Request(url)
res_data = urllib2.urlopen(req)
res = json.loads(res_data.read())

#获取类名
arr=res['data']
file_path=sys.path[0]+'/class/class'
if(not os.path.exists(file_path)):
    os.makedirs(file_path)
for className in arr:
    print "生成类名:".decode('utf-8')+className
    f = open(sys.path[0]+'/class/class/'+className+'.h', 'w')
    f.write('\n\n#import <UIKit/UIKit.h>\n\n\n@interface '+className+' : UIView\n\n\n@end')
    f.close()
    f = open (sys.path[0]+'/class/class/'+className + '.m', 'w')
    f.write ('\n\n#import "'+className+'.h"\n\n\n@implementation  '+className+' \n\n\n@end')
    f.close ()

