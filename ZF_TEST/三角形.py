#! /usr/bin/env python
#coding=GB18030

'''
打印倒三角形
'''
ceng=5
while ceng>=1:
    print('*'*ceng)
    ceng-=1

print('-'*30)    
#正三角形
ceng=1
while ceng<=5:
    print('*'*ceng)
    ceng+=1

#方式二：
ceng=1
while ceng<=5:
    count=1
    while count<=ceng:
        print('*',end='')
        count+=1
    ceng+=1
    print()