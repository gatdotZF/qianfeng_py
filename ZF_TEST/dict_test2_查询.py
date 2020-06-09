#! /usr/bin/env python
#coding=GB18030
'''
查询元素：
list1[index]--->element
dict1[key]--->value
'''
list1=[3,5,7,8]
print(list1[2])     #列表中查找元素根据下标查询

dict1={'0':'张三','1':'李四','2':'王五'}
print(dict1['2'])


'''
查询考试成绩大于90分的
'''
dict2={'张三':100,'李四':89,'oye':90,'lili':85}
for i in dict2.items():
    print(i)
    
for key,value in dict2.items():
    if value>=90:
        print(key)