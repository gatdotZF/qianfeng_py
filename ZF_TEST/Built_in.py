#! /usr/bin/env python
#coding=GB18030
 
# a=5
# b=6
# result=(a+b) if a<b else (b-a)
# print(result)
 
#################�����#########################
# import random
# print('*'*30,'�����','*'*30)
# for i in range(8):
#     print(random.randint(1,10))
# print('*'*60)
 
#################################################
 
print('#'*20,'��ӡ������','#'*30)
 
#��ʽһ��ֱ��������
ceng=1
while ceng<=5:
    print('*'*ceng)
    ceng+=1
print('#'*60)
# 
# #��ʽ��:ֱ��������
ceng=1
while ceng<=5:
    count=1
    while count<= ceng:
        print('*',end='')
        count+=1
    ceng+=1
    print()
print('*'*50)
###############################################
 
# name='lili'
# content='hello world!'
# 
# print('%s˵��%s'%(name,content))
################�б�����#####################
print('*'*20,'�б�����','*'*20)
print('�б���:1.ע����ֵ˳������5:0���޷�ȡֵ������5:0��ȡֵ')
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1[-1:-5:-1])
print('*'*50)
 
############�ڽ�����######################
print('*'*20,'�ڽ�������1.��Сд���','*'*20)
msg='onon owenio'
print('���ַ�����һ���ַ�ת���ɴ�д��',msg.capitalize())
 
print('���⻯��',msg.title())
 
print('�Ƿ���⻯��',msg.istitle())
 
print('ȫ����д��',msg.upper())
 
print('ȫ��Сд��',msg.lower())
   
print('*'*20,'�ڽ�������2.������غ������滻','*'*20)
S1='index lucy lucky goods!'
str_1=S1.find('R')    #������ֵ��'-1'������û�в��ҵ���rfind������ұ߿�ʼ���ң�lfind�������߿�ʼ����
print(str_1)
# 
print(S1.index('R'))  #��find()�������ƣ���str�����ַ����лᱨһ���쳣
 
print(S1.replace('c','2',1))  #�滻��old,new,[,max]��
  
print('*'*20,'�ڽ�������3.����-����(encode,decode)','*'*20)
msg='�Ͽ������������Σ�'
result=msg.encode('utf_8')  #�õ�b��ͷ�ģ����� ���������ã����Ļ��漰�������⣬GBK���ģ�gb1312�������ģ�unicodeͳһ�Ա�׼����
print(result)
print(result.decode('utf-8'))  #���룬��������ʽһ��
  
print('*'*20,'�ڽ�������4.startswith,endswith','*'*20)
filename='�ʼǱ�.doc'
result=filename.startswith('��')  #�ж���ʲô��ʼ�����ִ�Сд
print(result)
result=filename.endswith('doc')  #�ж���ʲô��β�����ִ�Сд
print(result)
  
print('*'*20,'�ڽ�������5.isalpha()��isdigit()','*'*20)
s='abcd'
result=s.isalpha()    #�ж��ַ����Ƿ�����ĸ,����True,False
print(result)
result=s.isdigit()    #�ж��ַ����Ƿ������֣�����True,False
print(result)
 
print('*'*20,'�ڽ�������6.join()','*'*20)
list1=['a','b','c','d']
result='-'.join(list1)      #��list1�е��ַ��á�-������
print(result)
 
print('*'*20,'�ڽ�������7.strip()��ȡ�ո�','*'*20)
s='  hello  '
print(s.strip())     #rstrip �ǽ�ȡ�ұ߿ո�lstrip��ȡ��߿ո�stripͬʱִ��rstrip()��lstrip()
 
print('*'*20,'�ڽ�������8.split()�ָ��ַ���','*'*20)
s='hello world hello kitty'
result=s.split(' ',2)     #�ָ��ַ��������ָ����ַ����������б���split('�ָ��'������)
print(result)
n=s.count(' ')       #count(args)���ַ�����ָ��args�ĸ���
print('n=',n)
  
print('*'*20,'�ڽ�������9.input()����','*'*20)
s1=input('�������һ���ַ�s1=��')
s2=input('������ڶ����ַ�s2=��')
s3=''
#��ʽһ��
for i in s1:
    if i not in s2:
        s3+=i
    s1=s3
print(s1)
 
# #��ʽ����
# for i in s2:
#     s1=s1.replace(i, '')
# print(s1)
 
#��ʽ����
# print(s3)
# for i in s2:
#     if i not in s3:
#         s3+=i
# for i in s3:
#     s1=s1.replace(i,'')
# print('s1=',s1)
 
 
 
 
 
 
 


