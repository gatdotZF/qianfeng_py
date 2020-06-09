#! /usr/bin/env python
#coding=GB18030
'''
列举，枚举
函数用于将一个可遍历的数据对象(如：列表，元组或字符串)组合为一个索引序列-index,value
'''
print('#'*15,'列举，枚举','#'*15)
l1=['a','b','tt','cwr']
for index,value in enumerate(l1):         #枚举，列表
    print(index,value)
for index,value in enumerate('happy'):    #枚举，字符串
    print(index,value)
    
'''
冒泡排序
'''
print('#'*15,'冒泡排序','#'*15)
numbers=[5,3,7,1,8,4,0]

#自定义排序方法（升序）

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]>numbers[j]:
            numbers[i],numbers[j]=numbers[j],numbers[i]
print('升序排序：',numbers)

#自定义排序方法（降序）

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]<numbers[j]:
            numbers[i],numbers[j]=numbers[j],numbers[i]
print('降序排序：',numbers)

#方式二：冒泡排序
for i in range(len(numbers)-1):
    #每一轮的比较，注意range的变化，这里需要进行length-1-i的比较，注意-i的意义（可以减少比较已经排好序的元素）
    for j in range(0,len(numbers)-1-i):    
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
print('升序排序：',numbers)
