#! /usr/bin/env python
#coding=GB18030

'''
系统函数 isinstance：判断是不是什么类型
    1. isinstance(变量，类型关键字) 
    2.返回值为False、True

'''
tuple1=(1,33,5,3,8)
print(isinstance(2,int))
print(isinstance(tuple1,tuple))

'''
1. 定义一个函数：参数username,password
2. 函数体
3. 判断函数传过来的username,password是否正确，如果正确则登录成功，否则登录失败；
'''
def login(username,password):
    #定义usname,PWD
    usname='admin1234'
    pwd='112233'
    while True:
        if username==usname and password == pwd:
            print('登录成功！')
            break
        else:
            print('登录失败！')
            username=input('请输入用户名：')
            password=input('请输入密码：')

username=input('请输入用户名：')
password=input('请输入密码：')
login(username,password)