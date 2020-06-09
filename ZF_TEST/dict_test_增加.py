#! /usr/bin/env python
#coding=GB18030

dict1={}
dict2=dict()    #空字典
print(dict2)

dict3={'ID':4206841111111,'name':'lucky','age':18}
dict4=dict([('name','231qw'),('age',18)])     #列表转成dict形式
print(dict4)  

list1=[(1,2),(3,4)]
print(dict(list1))    #注意：列表list可以转换成dict，但是前提列表中元素要成对出现

#增加
dict5={}
dict5['brand']='huawei'
print(dict5)
dict5['brand']='mi'
dict5['type']='p30 pro'
dict5['color']='黑色'
print(dict5)