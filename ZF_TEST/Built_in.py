#! /usr/bin/env python
#coding=GB18030
 
# a=5
# b=6
# result=(a+b) if a<b else (b-a)
# print(result)
 
#################随机数#########################
# import random
# print('*'*30,'随机数','*'*30)
# for i in range(8):
#     print(random.randint(1,10))
# print('*'*60)
 
#################################################
 
print('#'*20,'打印三角形','#'*30)
 
#方式一：直角三角形
ceng=1
while ceng<=5:
    print('*'*ceng)
    ceng+=1
print('#'*60)
# 
# #方式二:直角三角形
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
# print('%s说：%s'%(name,content))
################列表排序#####################
print('*'*20,'列表排序','*'*20)
print('列表倒序:1.注意数值顺序：正向5:0就无法取值，反向5:0可取值')
list1=[1,2,3,4,5,6,7,8,9,10]
print(list1[-1:-5:-1])
print('*'*50)
 
############内建函数######################
print('*'*20,'内建函数：1.大小写相关','*'*20)
msg='onon owenio'
print('将字符串第一个字符转换成大写：',msg.capitalize())
 
print('标题化：',msg.title())
 
print('是否标题化：',msg.istitle())
 
print('全部大写：',msg.upper())
 
print('全部小写：',msg.lower())
   
print('*'*20,'内建函数：2.查找相关函数、替换','*'*20)
S1='index lucy lucky goods!'
str_1=S1.find('R')    #若返回值是'-1'，代表没有查找到，rfind代表从右边开始查找，lfind代表从左边开始查找
print(str_1)
# 
print(S1.index('R'))  #跟find()方法类似，若str不在字符串中会报一个异常
 
print(S1.replace('c','2',1))  #替换【old,new,[,max]】
  
print('*'*20,'内建函数：3.编码-解码(encode,decode)','*'*20)
msg='上课啦，认真听课！'
result=msg.encode('utf_8')  #得到b开头的，编码 ，网络运用，中文会涉及编码问题，GBK中文，gb1312简体中文，unicode统一性标准编码
print(result)
print(result.decode('utf-8'))  #解码，编码解码格式一致
  
print('*'*20,'内建函数：4.startswith,endswith','*'*20)
filename='笔记本.doc'
result=filename.startswith('笔')  #判断以什么开始，区分大小写
print(result)
result=filename.endswith('doc')  #判断以什么结尾，区分大小写
print(result)
  
print('*'*20,'内建函数：5.isalpha()、isdigit()','*'*20)
s='abcd'
result=s.isalpha()    #判断字符串是否是字母,返回True,False
print(result)
result=s.isdigit()    #判断字符串是否是数字，返回True,False
print(result)
 
print('*'*20,'内建函数：6.join()','*'*20)
list1=['a','b','c','d']
result='-'.join(list1)      #将list1中的字符用‘-’连接
print(result)
 
print('*'*20,'内建函数：7.strip()截取空格','*'*20)
s='  hello  '
print(s.strip())     #rstrip 是截取右边空格，lstrip截取左边空格，strip同时执行rstrip()、lstrip()
 
print('*'*20,'内建函数：8.split()分割字符串','*'*20)
s='hello world hello kitty'
result=s.split(' ',2)     #分割字符串，将分割后的字符串保存在列表中split('分割符'，次数)
print(result)
n=s.count(' ')       #count(args)求字符串中指定args的个数
print('n=',n)
  
print('*'*20,'内建函数：9.input()输入','*'*20)
s1=input('请输入第一个字符s1=：')
s2=input('请输入第二个字符s2=：')
s3=''
#方式一：
for i in s1:
    if i not in s2:
        s3+=i
    s1=s3
print(s1)
 
# #方式二：
# for i in s2:
#     s1=s1.replace(i, '')
# print(s1)
 
#方式三：
# print(s3)
# for i in s2:
#     if i not in s3:
#         s3+=i
# for i in s3:
#     s1=s1.replace(i,'')
# print('s1=',s1)
 
 
 
 
 
 
 


