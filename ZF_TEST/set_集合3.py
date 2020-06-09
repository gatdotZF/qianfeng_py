#! /usr/bin/env python
#coding=GB18030

'''
已知两个列表：
l1=[5,1,2,9,0,3]
l2=[7,2,5,7,9]

找出两个列表的不同元素   
    1. s1^s2 对称差集
    2. sysmmetric_difference()  对称差集函数

找出两个列表公共元素
    1. &
    2. intersection()

'''

l1=[5,1,2,9,0,3]
l2=[7,2,5,7,9]
s1=set(l1)
s2=set(l2)
print(s1)
print(s2)

#对称差集
result=(s1|s2)-(s1&s2)
print('不同元素：',result)

result=s1 ^ s2   #对称差集
print('不同元素',result)
print('相同元素：',s1.intersection(s2))


'''
1.差集并赋值
    difference_update()  #找出差集，并自动更新
    s1=s1.difference(s2)
    print(s1)
    
    s1.difference_update(s2)  
2.交集并赋值
    intersection_update()
3.并集并赋值
    union_update()
4.对称集并赋值
    symmetric_difference_update()
'''
s1.difference_update(s2)    #差集
print(s1)    

'''

'''