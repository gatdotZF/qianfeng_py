#! /usr/bin/env python
#coding=GB18030

'''
��֪�����б�
l1=[5,1,2,9,0,3]
l2=[7,2,5,7,9]

�ҳ������б�Ĳ�ͬԪ��   
    1. s1^s2 �ԳƲ
    2. sysmmetric_difference()  �ԳƲ����

�ҳ������б���Ԫ��
    1. &
    2. intersection()

'''

l1=[5,1,2,9,0,3]
l2=[7,2,5,7,9]
s1=set(l1)
s2=set(l2)
print(s1)
print(s2)

#�ԳƲ
result=(s1|s2)-(s1&s2)
print('��ͬԪ�أ�',result)

result=s1 ^ s2   #�ԳƲ
print('��ͬԪ��',result)
print('��ͬԪ�أ�',s1.intersection(s2))


'''
1.�����ֵ
    difference_update()  #�ҳ�������Զ�����
    s1=s1.difference(s2)
    print(s1)
    
    s1.difference_update(s2)  
2.��������ֵ
    intersection_update()
3.��������ֵ
    union_update()
4.�ԳƼ�����ֵ
    symmetric_difference_update()
'''
s1.difference_update(s2)    #�
print(s1)    

'''

'''