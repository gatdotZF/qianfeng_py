#! /usr/bin/env python
#coding=GB18030

'''
    1. 产生10个1~20的随机数，去除里面的重复项；
    2.键盘输入一个元素，将此元素从不重复的集合中删除
'''
import random
#方式一：
# list1=[]
# set1=set()
# for i in range(10):
#     ran=random.randint(1,20)
#     list1.append(ran)
# set1.update(list1)
# print(list1)
# print(set1)
# 
# #方式二：
# list1=[]
# for i in range(10):
#     ran= random.randint(1,20)
#     list1.append(ran)
# list1=set(list1)
# print(list1)
# 
# num=int(input('请输入一个数字：'))
# set1.discard(num)
# print('删除之后的结果：',set1)

#方式三：
set1=set()
for i in range(10):
    ran=random.randint(1,20)
    set1.add(ran)
print(set1)
 
num=int(input('请输入一个数字：'))
set1.discard(num)
print('删除之后的结果：',set1)

'''
其他：符号操作
    in
        （+ * 不支持）  |
    - 差集         set1=set3-set2
    difference 差集   set1=set3.difference(set2)
    &交集      set1=set3 & set2
    intersection()  交集   set1=set3.intersection(set2)
    | 并集   set1=set3 | set2
    union 并集 set1=set3.union(set2)
'''
#其他：符号操作
print(6 in set1)

set2={2,3,4,5,6}
set3={2,3,4,5,6,7}
print(set2==set3)   #判断两个集合的内容是否相等

#测试：print(set2 !=set3)  
# （+ * 不支持） - & |
# set4=set2+set3     #不存在，会报错
# print(set4)

# set5=set2*2      #不支持
# print(set5)

# - 差集
set4=set2-set3
set5=set3-set2     #差集，不一样的集合
print(set4,set5)
 
#difference 差集
set6=set3.difference(set2)  #difference差集
print(set6)

# &交集   intersection()
set7=set2 & set3
print(set7)
 
set8=set3.intersection(set2)
print(set8)
# 
# # | 并集  union()  联合
set9 = set3 | set2
print("————>",set9)
 
set10 = set3.union(set2)
print(set10)


