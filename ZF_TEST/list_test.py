#! /usr/bin/env python
#coding=GB18030

import random
#################list#################
brands=['huawei','iphone','dell','hp','mac','����']
print('*'*20,'1.list:�滻','*'*20)
for i in range(len(brands)):      #�б��滻���±�������±귽ʽ
    if 'hua' in brands[i]:
        brands[i]='HUAWEI'
print(brands)

print('*'*20,'2.list:ɾ��','*'*20)
l=len(brands)
i=0
while i<l:
    if 'hp' in brands[i] or 'mac' in brands[i]:
        del brands[i]
        l-=1
        continue            #Ҳ����i-=1,��Ϊ����©ɾ������
    i+=1
print(brands)
'''
for word in words:       #in [....]�ж������Ƿ����б���
    if w in word:        #in ' '�ж��ַ���w�Ƿ���word��
'''

print('*'*20,'3.list:��Ƭ','*'*20)
s='abcdefghij'
s1=s[2:4]
print('�ַ�����Ƭs1:',s1)
list1=['a','b','c','d']
print('list1[2:5]������Ƭ:',list1[2:5])
print('list1[-1::-1]������Ƭ:',list1[-1::-1])
print('list1[0::1]������Ƭ:',list1[0::1])   

print('*'*20,'4.list:���append��extended��insert','*'*20)
'''
append():ĩβ׷��
extended():�������б�ĺϲ���һ����Ӷ��Ԫ��
insert():����
'''
girls=['����','١���','����']
# print('-'*3,'4.1 list:���append()','-'*3)
# name=input('��������ϲ����Ů��������:')
# girls.append(name)             #appendĩβ׷��
# print(girls)

print('-'*3,'4.2 list:���extended()','-'*3)
names=['����','������']
girls.extend(names)              #�������б�ĺϲ���һ����Ӷ��Ԫ��
# girls=girls+names              #���š�+��Ҳ�������б�ĺϲ�
print(girls)

print('-'*3,'4.3 list:���insert()-����','-'*3)
girls.insert(2,'uouu')           #ָ��λ�ò���Ԫ��
print(girls)

'''
list:���ֵ��Сֵԭ��
max_value=max(random_list)
min_value=min(random_list)

list:�Զ������ֵ
����:max_value=random_list[0]
for value in random_list:
    if value>max_value:
        max_value=vaule

list:�Զ�����Сֵ
���裺min_value=random_list[0]
for value in random_list:
    if value<min_value:
        min_value=value        
'''
print('*'*20,'5.list:sum()���','*'*20)
'''
he=sum(random_list)
sum=0
for value in random_list:
    sum+=value
'''

sum=0
for i  in range(1,50):
    sum+=i
print(sum)

print('*'*20,'6.list:sort()����','*'*20)
'''
new_list=sorted(random_list)----����
new_list=sorted(random_list,reverse=Ture)  ----����
'''
# random_list=[1,4,-3,8,0,67]
random_list=['Ga','2A','BC','D','G']
print('new_list����:',sorted(random_list))
print('new_list����:',sorted(random_list,reverse=True))

print('*'*20,'7.list:����ת��','*'*20)
'''
int(x)    ��xת����һ������
long(x)   ��xת����һ��������
float(x)  ��xת����һ��������
str(x)    ��xת�����ַ���
list(s)   ������sת����һ���б�
ord(x)    ��һ���ַ���ת������������ֵ
hex(x)    ��һ������ת��Ϊһ��ʮ�������ַ���
oct(x)    ��һ������ת����һ���˽����ַ���

int is not iterable(���Ͳ��ɵ������޷�ת�����б�)
��for ���� in�����ѭ�����ǿɵ�����
for i in range(s):
    pass

'''
s='abc'
result=list(s)
print('strת����list:',result)
