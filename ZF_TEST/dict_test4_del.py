#! /usr/bin/env python
#coding=GB18030

'''
���ú�����
    dict.keys()             ��ȡkeysֵ
    dict.values()           ��ȡvaultsֵ
    dict.items()            ��ȡ��ֵ��(key,vault)
    dict.get(key[,default])  ��ȡkeyֵvalue,��dict����keyֵ���򷵻ض�Ӧ��valueֵ�����ޣ��򷵻�None��
                                                                        ����defaultֵ����dict����keyֵ���򷵻ض�Ӧ��valueֵ�����ޣ��򷵻�defaultֵ��

'''
dict1={'0':'����','1':'����','2':'����'}
print('ww' in dict1.items())
result=dict1.get('onon',10)
print(result)

'''
ɾ�����ú�����
    del dict[key]
    dict.pop(key[,default])  --->����keyɾ���ֵ��еļ�ֵ�ԣ�����ֵ��value��ֻҪɾ���ɹ����򷵻ؼ�ֵ�Ե�ֵValue
                            pop��Ĭ��ֵ����������ɾ����ֵû���ҵ���Ӧ��key,�򷵻�defaultĬ��ֵ
    dict.popitem() ---->���ɾ���ֵ��еļ�ֵ�ԣ�һ���ĩβɾ��Ԫ�أ�
    dict.clear()  ----->ͬ�б��clear()
dict����remove����
'''

del dict1['0']
print(dict1)
# del dict1['hhhh']    #keyError
# print(dict1)
#dict1.remove('2')  #�����ڣ��ᱨ��

result=dict1.pop('2')    #����value
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
�������ú�����
 update()      []+[]�ϲ�����
               dict1=dict1+dict2  �����
 fromkeys(seq[,default])    ------>��seqת���ֵ���ʽ�����û��ָ��Ĭ�ϵ�value����None
                new_dict=dict.fromkeys(list1) ---> {'aa': None, 'bb': None, 'cc': None}
                            ------>��ָ��default������default���None���Valueֵ
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