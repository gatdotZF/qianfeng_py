#! /usr/bin/env python
#coding=GB18030

'''
    1. ����10��1~20���������ȥ��������ظ��
    2.��������һ��Ԫ�أ�����Ԫ�شӲ��ظ��ļ�����ɾ��
'''
import random
#��ʽһ��
# list1=[]
# set1=set()
# for i in range(10):
#     ran=random.randint(1,20)
#     list1.append(ran)
# set1.update(list1)
# print(list1)
# print(set1)
# 
# #��ʽ����
# list1=[]
# for i in range(10):
#     ran= random.randint(1,20)
#     list1.append(ran)
# list1=set(list1)
# print(list1)
# 
# num=int(input('������һ�����֣�'))
# set1.discard(num)
# print('ɾ��֮��Ľ����',set1)

#��ʽ����
set1=set()
for i in range(10):
    ran=random.randint(1,20)
    set1.add(ran)
print(set1)
 
num=int(input('������һ�����֣�'))
set1.discard(num)
print('ɾ��֮��Ľ����',set1)

'''
���������Ų���
    in
        ��+ * ��֧�֣�  |
    - �         set1=set3-set2
    difference �   set1=set3.difference(set2)
    &����      set1=set3 & set2
    intersection()  ����   set1=set3.intersection(set2)
    | ����   set1=set3 | set2
    union ���� set1=set3.union(set2)
'''
#���������Ų���
print(6 in set1)

set2={2,3,4,5,6}
set3={2,3,4,5,6,7}
print(set2==set3)   #�ж��������ϵ������Ƿ����

#���ԣ�print(set2 !=set3)  
# ��+ * ��֧�֣� - & |
# set4=set2+set3     #�����ڣ��ᱨ��
# print(set4)

# set5=set2*2      #��֧��
# print(set5)

# - �
set4=set2-set3
set5=set3-set2     #�����һ���ļ���
print(set4,set5)
 
#difference �
set6=set3.difference(set2)  #difference�
print(set6)

# &����   intersection()
set7=set2 & set3
print(set7)
 
set8=set3.intersection(set2)
print(set8)
# 
# # | ����  union()  ����
set9 = set3 | set2
print("��������>",set9)
 
set10 = set3.union(set2)
print(set10)


