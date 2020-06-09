#! /usr/bin/env python
#coding=GB18030

import random
#################list#################
brands=['huawei','iphone','dell','hp','mac','神州']
print('*'*20,'1.list:替换','*'*20)
for i in range(len(brands)):      #列表替换更新必须采用下标方式
    if 'hua' in brands[i]:
        brands[i]='HUAWEI'
print(brands)

print('*'*20,'2.list:删除','*'*20)
l=len(brands)
i=0
while i<l:
    if 'hp' in brands[i] or 'mac' in brands[i]:
        del brands[i]
        l-=1
        continue            #也可用i-=1,因为存在漏删除现象
    i+=1
print(brands)
'''
for word in words:       #in [....]判断内容是否在列表中
    if w in word:        #in ' '判断字符串w是否在word中
'''

print('*'*20,'3.list:切片','*'*20)
s='abcdefghij'
s1=s[2:4]
print('字符串切片s1:',s1)
list1=['a','b','c','d']
print('list1[2:5]正向切片:',list1[2:5])
print('list1[-1::-1]反向切片:',list1[-1::-1])
print('list1[0::1]正向切片:',list1[0::1])   

print('*'*20,'4.list:添加append、extended、insert','*'*20)
'''
append():末尾追加
extended():类似于列表的合并，一次添加多个元素
insert():插入
'''
girls=['杨幂','佟丽娅','董卿']
# print('-'*3,'4.1 list:添加append()','-'*3)
# name=input('请输入你喜欢的女明星名字:')
# girls.append(name)             #append末尾追加
# print(girls)

print('-'*3,'4.2 list:添加extended()','-'*3)
names=['朱涛','王丽坤']
girls.extend(names)              #类似于列表的合并，一次添加多个元素
# girls=girls+names              #符号‘+’也可用于列表的合并
print(girls)

print('-'*3,'4.3 list:添加insert()-插入','-'*3)
girls.insert(2,'uouu')           #指定位置插入元素
print(girls)

'''
list:最大值最小值原理
max_value=max(random_list)
min_value=min(random_list)

list:自定义最大值
假设:max_value=random_list[0]
for value in random_list:
    if value>max_value:
        max_value=vaule

list:自定义最小值
假设：min_value=random_list[0]
for value in random_list:
    if value<min_value:
        min_value=value        
'''
print('*'*20,'5.list:sum()求和','*'*20)
'''
he=sum(random_list)
sum=0
for value in random_list:
    sum+=value
'''

sum=0
for i  in range(1,50):
    sum+=i
print(sum)

print('*'*20,'6.list:sort()排序','*'*20)
'''
new_list=sorted(random_list)----升序
new_list=sorted(random_list,reverse=Ture)  ----降序
'''
# random_list=[1,4,-3,8,0,67]
random_list=['Ga','2A','BC','D','G']
print('new_list升序:',sorted(random_list))
print('new_list降序:',sorted(random_list,reverse=True))

print('*'*20,'7.list:类型转换','*'*20)
'''
int(x)    将x转换成一个整数
long(x)   将x转换成一个长整型
float(x)  将x转换成一个浮点数
str(x)    将x转换成字符串
list(s)   将序列s转换成一个列表
ord(x)    将一个字符串转换成它的整数值
hex(x)    将一个整数转换为一个十六进制字符串
oct(x)    将一个整数转换成一个八进制字符串

int is not iterable(整型不可迭代，无法转换成列表)
在for …… in里面可循环，是可迭代的
for i in range(s):
    pass

'''
s='abc'
result=list(s)
print('str转换成list:',result)
