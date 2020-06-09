#! /usr/bin/env python
#coding=GB18030

'''
内置函数：
    dict.keys()             获取keys值
    dict.values()           获取vaults值
    dict.items()            获取键值对(key,vault)
    dict.get(key[,default])  获取key值value,若dict中有key值，则返回对应的value值。若无，则返回None；
                                                                        若给default值，若dict中有key值，则返回对应的value值。若无，则返回default值；

'''
dict1={'0':'张三','1':'李四','2':'王五'}
print('ww' in dict1.items())
result=dict1.get('onon',10)
print(result)

'''
删除内置函数：
    del dict[key]
    dict.pop(key[,default])  --->根据key删除字典中的键值对，返回值是value。只要删除成功，则返回键值对的值Value
                            pop的默认值，往往是在删除的值没有找到对应的key,则返回default默认值
    dict.popitem() ---->随机删除字典中的键值对（一般从末尾删除元素）
    dict.clear()  ----->同列表的clear()
dict中无remove函数
'''

del dict1['0']
print(dict1)
# del dict1['hhhh']    #keyError
# print(dict1)
#dict1.remove('2')  #不存在，会报错

result=dict1.pop('2')    #返回value
print(result)     
print(dict1)

result=dict1.pop('onoo',80)
print('====>',result)
print(dict1)

print('*'*30)
#popitem()
dict2={'7':'mokey','8':'tom','9':'wono'}
result=dict2.popitem()
print(result)
print(dict2)

dict2.clear()
print(dict2)

'''
其他内置函数：
 update()      []+[]合并操作
               dict1=dict1+dict2  报错的
 fromkeys(seq[,default])    ------>将seq转成字典形式，如果没有指定默认的value则用None
                new_dict=dict.fromkeys(list1) ---> {'aa': None, 'bb': None, 'cc': None}
                            ------>若指定default，则用default替代None这个Value值
                new_dict=dict.fromkeys(list1,10) ---> {'cc': 10, 'aa': 10, 'bb': 10}
''' 
#update
dict1={0:'tongm',1:'jkey',2:'lucy'}
dict2={0:'lili','4':'ruby'}
result=dict1.update(dict2)
print(result)
print(dict1)

#fromkeys
list1=['aa','bb','cc']
new_dict=dict.fromkeys(list1,10)
print(new_dict)