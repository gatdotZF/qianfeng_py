#! /usr/bin/env python
#coding=GB18030

'''
���ϣ�
    �ؼ��֣�set ����Ĳ��ظ��� s1=set()
   ���ã�ȥ��
   ���ú�����
              ���ӣ�add()  update()
              ɾ����remove() discard() pop() clear()
             ���㣺
        difference()�  ----> ��Ӧ���� -
        intersection()����-----> ��Ӧ���� &
        union() ����  ------>��Ӧ���� |
        symmetric_diffrence() �ԳƼ�--->��Ӧ���� ^
    ��ɾ�Ĳ飺
      1.����     s1=set()
      s1.add() ���һ��Ԫ��
      s1.update()  ����Ӷ��Ԫ��
      2.ɾ��
        remove()  ���Ԫ�ش�����ɾ�����������򱨴�
        pop() ���ɾ����һ��ɾ����һ��Ԫ�أ�
        clear()  ���
        discard()  ������remove,�Ƴ������ڵ�Ԫ��ʱ�򲻻ᱨ��
        ���ţ�
                ��֧��+ *
                ֧�֣�- & | ^  
'''

# #���ظ��ر�
# list1=[3,5,4,12,3,8,7,9,9,2,5]
# #��������:Set
# s1=set()
# s2={1,3,7}  #�ֵ䣺{key:value,key:value,key:value����} ���ϣ�{Ԫ��1��Ԫ��2��Ԫ��3����}
# print(type(s2))
# 
# #Ӧ�ã������һ���б����ȥ�� set()
# print(set(list1))

#��ɾ�Ĳ�
#1. ����
s1=set()
s1.add('hello')
s1.add('С������')
s1.add('lucy')
print(s1)

#update()  ����Ӷ��Ԫ��
t1=('linzhiling','�Գ���')
s1.update(t1)
print(s1)
s1.add(t1)
print(s1)

#2. ɾ��  remove pop clear����
s1.remove('linzhiling')
print(s1)

# s1.remove('woeno')    #remove �����ڵ�Ԫ�أ��ᱨ��
# print(s1)

#pop
s1.pop()
print(s1)
s1.pop()
print(s1)

#clear ���
s1.clear()
print(s1)

#discard()  ������remove()�����Ƴ������ڵ�Ԫ��ʱ������

s1.discard('ononoo')
print(s1)