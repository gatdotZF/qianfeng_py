#! /usr/bin/env python
#coding=GB18030

'''
�û�ע�Ṧ��
�����û���
��������
��������
�����ֻ���
'''
print('--------------��ӭ����������Ƹ�û�ע��--------------')
database=[]
while True:
    username=input('�������û�����')
    password=input('���������룺')
    repassword=input('���ٴ��������룺')
    email=input('���������䣺')
    phone=input('�������ֻ��ţ�')
    
    #����һ���ֵ�
    user={}
    user['username']=username
    if password ==repassword:
        user['password']=password
    else:
        print('�������벻һ�£����������룡')
        continue
    user['email']=email
    user['phone']=phone
    
    #���浽���ݿ�
    database.append(user)
    answer=input('�Ƿ����ע�᣿��y/n��\n')
    if answer !='y':
        break
print(database)