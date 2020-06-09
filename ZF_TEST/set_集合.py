#! /usr/bin/env python
#coding=GB18030

'''
集合：
    关键字：set 无序的不重复的 s1=set()
   作用：去重
   内置函数：
              增加：add()  update()
              删除：remove() discard() pop() clear()
             运算：
        difference()差集  ----> 对应符号 -
        intersection()交集-----> 对应符号 &
        union() 并集  ------>对应符号 |
        symmetric_diffrence() 对称集--->对应符号 ^
    增删改查：
      1.增加     s1=set()
      s1.add() 添加一个元素
      s1.update()  可添加多个元素
      2.删除
        remove()  如果元素存在则删除，不存在则报错
        pop() 随机删除（一般删除第一个元素）
        clear()  清空
        discard()  类似于remove,移除不存在的元素时候不会报错
        符号：
                不支持+ *
                支持：- & | ^  
'''

# #不重复特别：
# list1=[3,5,4,12,3,8,7,9,9,2,5]
# #声明集合:Set
# s1=set()
# s2={1,3,7}  #字典：{key:value,key:value,key:value……} 集合：{元素1，元素2，元素3……}
# print(type(s2))
# 
# #应用：如果有一个列表快速去重 set()
# print(set(list1))

#增删改查
#1. 增加
s1=set()
s1.add('hello')
s1.add('小猪佩奇')
s1.add('lucy')
print(s1)

#update()  可添加多个元素
t1=('linzhiling','言承旭')
s1.update(t1)
print(s1)
s1.add(t1)
print(s1)

#2. 删除  remove pop clear……
s1.remove('linzhiling')
print(s1)

# s1.remove('woeno')    #remove 不存在的元素，会报错
# print(s1)

#pop
s1.pop()
print(s1)
s1.pop()
print(s1)

#clear 清空
s1.clear()
print(s1)

#discard()  类似于remove()，在移除不存在的元素时不报错

s1.discard('ononoo')
print(s1)