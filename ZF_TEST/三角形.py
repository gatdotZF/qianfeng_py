#! /usr/bin/env python
#coding=GB18030

'''
��ӡ��������
'''
ceng=5
while ceng>=1:
    print('*'*ceng)
    ceng-=1

print('-'*30)    
#��������
ceng=1
while ceng<=5:
    print('*'*ceng)
    ceng+=1

#��ʽ����
ceng=1
while ceng<=5:
    count=1
    while count<=ceng:
        print('*',end='')
        count+=1
    ceng+=1
    print()