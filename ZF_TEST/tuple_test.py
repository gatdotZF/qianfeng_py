#! /usr/bin/env python
#coding=GB18030


# import random
# list1=[]
# for i in range(10):
#     ran1=random.randint(1,20)
#     list1.append(ran1)
# tuple1=tuple(list1)
# #�б�ת����Ԫ��
# print(tuple1,type(tuple1))
# #��ѯ���±ꡢ��Ƭ[:]
# print(tuple1[2])
# print(tuple1[2:-2])
# print(tuple1[::-1])
# #���ֵ����Сֵ
# max_vaule=max(tuple1)
# min_vaule=min(tuple1)
# print('max_vaule:{}     min_vaule:{}'.format(max_vaule,min_vaule))
# 
# #���
# sum_total=sum(tuple1)
# print('sum=',sum_total)
# print('len=',len(tuple1))
# #Ԫ���к���
# print('count=1������',tuple1.count(1))  #��ѯԪ���С�1���ĸ���
# print('index=1���±꣺',tuple1.index(1))  #����Ԫ����4���±�λ�ã���Ԫ�����޴�Ԫ�ػᱨ��

#���-װ��
t1=(4,7,3)
a,b,c=t1
print(a,b,c)

t1=(2,5,8,9,7)
a,*_,c=t1
print(a,c,_)

t1=(9,)
a,*b=t1
print(a,b)   #*b��ʾδ֪����0~n,0-->[]�����Ԫ��-->[Ԫ��1��Ԫ��2]

#�ַ���
x,y,*z='hello'
print(x,y,z)

#�б�
x,y,*z=['aa',6,'hello','good','happy']
print(x,y,z)

'''
print(*y)
print(*[4,8,6])---->�����4 8 6
��ֵ��װ��
*y=4,6,8
ϵͳ��ɢ�� --->[]--->[4,8,6]
��ӡ��
print(*[4,8,6]) --->���  4 8 6 
'''
x,*y=(9,4,8,6)
print(x,y)
print(*y)

t2=(3,4)+(1,2)
print(t2)
t3=(7,8)*2
print(t3)
print(t2 is t3)
print(3 in t2)
print(3 not in t3)
print(sorted(t2))
print(tuple(sorted(t2)))