#! /usr/bin/env python
#coding=GB18030
'''
��ѯԪ�أ�
list1[index]--->element
dict1[key]--->value
'''
list1=[3,5,7,8]
print(list1[2])     #�б��в���Ԫ�ظ����±��ѯ

dict1={'0':'����','1':'����','2':'����'}
print(dict1['2'])


'''
��ѯ���Գɼ�����90�ֵ�
'''
dict2={'����':100,'����':89,'oye':90,'lili':85}
for i in dict2.items():
    print(i)
    
for key,value in dict2.items():
    if value>=90:
        print(key)