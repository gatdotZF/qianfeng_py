#! /usr/bin/env python
#coding=GB18030

'''
ϵͳ���� isinstance���ж��ǲ���ʲô����
    1. isinstance(���������͹ؼ���) 
    2.����ֵΪFalse��True

'''
tuple1=(1,33,5,3,8)
print(isinstance(2,int))
print(isinstance(tuple1,tuple))

'''
1. ����һ������������username,password
2. ������
3. �жϺ�����������username,password�Ƿ���ȷ�������ȷ���¼�ɹ��������¼ʧ�ܣ�
'''
def login(username,password):
    #����usname,PWD
    usname='admin1234'
    pwd='112233'
    while True:
        if username==usname and password == pwd:
            print('��¼�ɹ���')
            break
        else:
            print('��¼ʧ�ܣ�')
            username=input('�������û�����')
            password=input('���������룺')

username=input('�������û�����')
password=input('���������룺')
login(username,password)