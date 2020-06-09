#! /usr/bin/env python
#coding=GB18030


# import random
# list1=[]
# for i in range(10):
#     ran1=random.randint(1,20)
#     list1.append(ran1)
# tuple1=tuple(list1)
# #列表转换成元组
# print(tuple1,type(tuple1))
# #查询，下标、切片[:]
# print(tuple1[2])
# print(tuple1[2:-2])
# print(tuple1[::-1])
# #最大值，最小值
# max_vaule=max(tuple1)
# min_vaule=min(tuple1)
# print('max_vaule:{}     min_vaule:{}'.format(max_vaule,min_vaule))
# 
# #求和
# sum_total=sum(tuple1)
# print('sum=',sum_total)
# print('len=',len(tuple1))
# #元组中函数
# print('count=1个数：',tuple1.count(1))  #查询元组中‘1’的个数
# print('index=1的下标：',tuple1.index(1))  #查找元组中4的下标位置，若元组中无此元素会报错

#拆包-装包
t1=(4,7,3)
a,b,c=t1
print(a,b,c)

t1=(2,5,8,9,7)
a,*_,c=t1
print(a,c,_)

t1=(9,)
a,*b=t1
print(a,b)   #*b表示未知个数0~n,0-->[]，多个元素-->[元素1，元素2]

#字符串
x,y,*z='hello'
print(x,y,z)

#列表
x,y,*z=['aa',6,'hello','good','happy']
print(x,y,z)

'''
print(*y)
print(*[4,8,6])---->拆包，4 8 6
赋值：装包
*y=4,6,8
系统：散列 --->[]--->[4,8,6]
打印：
print(*[4,8,6]) --->拆包  4 8 6 
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