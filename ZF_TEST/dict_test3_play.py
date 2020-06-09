#! /usr/bin/env python
#coding=GB18030

'''
用户注册功能
输入用户名
输入密码
输入邮箱
输入手机号
'''
print('--------------欢迎来到智联招聘用户注册--------------')
database=[]
while True:
    username=input('请输入用户名：')
    password=input('请输入密码：')
    repassword=input('请再次输入密码：')
    email=input('请输入邮箱：')
    phone=input('请输入手机号：')
    
    #定义一个字典
    user={}
    user['username']=username
    if password ==repassword:
        user['password']=password
    else:
        print('两次密码不一致，请重新输入！')
        continue
    user['email']=email
    user['phone']=phone
    
    #保存到数据库
    database.append(user)
    answer=input('是否继续注册？（y/n）\n')
    if answer !='y':
        break
print(database)