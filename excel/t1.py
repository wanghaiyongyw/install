#encoding:utf-8
'''
import math

if __name__ == '__main__':
    n=raw_input("请输入您的编号：")
    print n
'''
#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import os,sys
reload(sys)
sys.setdefaultencoding('utf8')
contect={'北京':{'北京':['海淀','朝阳']},'河北':{'廊坊':['三河','香河']}}
print contect.keys()
while True:
    first=raw_input('请输入一级菜单名称: ')
    print first
    if first in contect.keys():
        print '你选择的是 %s' % first
        sec=raw_input('请输入二级菜单名称: ')
        if sec in contect[first].keys():
            print '你选择的是 %s 省得 %s' % (first,sec)
            third = raw_input('请输入你选择的三级菜单: ')
            if third in contect[first][sec]:
                print '您选择的是%s 省 %s 市 %s 县区'%(first,sec,third)
            else:
                re=raw_input('您选择的县区不在此范围，重新输入(yes/Y),退出(exit): ')
                if re == 'exit':
                    print '欢迎下次再次使用'
                    break
    else:
        break
