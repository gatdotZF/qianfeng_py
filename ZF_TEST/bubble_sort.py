#! /usr/bin/env python
#coding=GB18030
'''
�о٣�ö��
�������ڽ�һ���ɱ��������ݶ���(�磺�б�Ԫ����ַ���)���Ϊһ����������-index,value
'''
print('#'*15,'�о٣�ö��','#'*15)
l1=['a','b','tt','cwr']
for index,value in enumerate(l1):         #ö�٣��б�
    print(index,value)
for index,value in enumerate('happy'):    #ö�٣��ַ���
    print(index,value)
    
'''
ð������
'''
print('#'*15,'ð������','#'*15)
numbers=[5,3,7,1,8,4,0]

#�Զ������򷽷�������

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]>numbers[j]:
            numbers[i],numbers[j]=numbers[j],numbers[i]
print('��������',numbers)

#�Զ������򷽷�������

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]<numbers[j]:
            numbers[i],numbers[j]=numbers[j],numbers[i]
print('��������',numbers)

#��ʽ����ð������
for i in range(len(numbers)-1):
    #ÿһ�ֵıȽϣ�ע��range�ı仯��������Ҫ����length-1-i�ıȽϣ�ע��-i�����壨���Լ��ٱȽ��Ѿ��ź����Ԫ�أ�
    for j in range(0,len(numbers)-1-i):    
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
print('��������',numbers)
