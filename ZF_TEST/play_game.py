#! /usr/bin/env python
#coding=GB18030
import random
print('*'*15,'������ҫ','*'*15)
print('\t��ӭ����������ҫ��Ϸ')
role=input('��ѡ�����\n 1.³��\n 2.����\n 3.���\n 4.������\n 5.����\n 6.�����\n')
coins=1000
weapon_list=[]
print('��ӭ{}����������ҫ����ǰ�����{}'.format(role,coins))
while True:
    choice=int(input('��ѡ��\n 1.��������\n 2.����\n 3.ɾ������\n 4.�鿴����\n 5.�˳���Ϸ\n'))
    if choice==1:
#         pass
        print('\t��ӭ����������')
        weapons=[['98K',500],['������','400'],['ӣ��ǹ','600'],['���ǹ',1000]]
        for weapon in weapons:
            print(weapon[0],weapon[1],sep='   ')  #�м�������ո�
        #����Ҫ�������������
        weapon_name=input('������Ҫ�������������')
        if weapon_name not in weapon_list:
            for weapon in weapons:
                if weapon_name == weapon[0]:
                    if coins >=int(weapon[1]):
                        coins-=int(weapon[1])
                        weapon_list.append(weapon[0])
                        break
                    else:
                        print('��Ҳ��㣬��Ͻ������')
                else:
                    print('�����������ƴ���')
         
    elif choice==2:
        #������ӵ�ж������
        print('����ս������')
        if len(weapon_list)>0:
        #ѡ������
            print('{}ӵ�е��������£�{}'.format(role,weapon_list))
            for weapon in weapon_list:
                print(weapon)
            while True:
                weapon_name=input('��ѡ��')
                if weapon_name in weapon_list:
                    #����ս��״̬��Ĭ�ϸ��ŷ�
                    ran1=random.randint(1,20)  #�ŷ�
                    ran2=random.randint(1,20)  #role
                    if ran1>ran2:
                        print('�˾ֶ�ս���ŷ�ʤ����')
                    elif ran1==ran2:
                        print('�˾ֶ�ս��ƽ�֣�')
                    else:
                        print('�˾ֶ�ս��{}ʤ��'.format(role))
                        coins+=200
                    break   
                else:
                    print('ѡ������������ڣ�������ѡ��')
        else:
            print('��û�й����������Ͽ�ʹ�ý�ҹ��������ɣ�')        
    elif choice==3:
        #��ѯ������
        print('��ǰ�����⣺{}'.format(weapon_list))
        if len(weapon_list)>0:
            for weapon in weapon_list:
                print(weapon)
            while True:
                weapon_name=input('������Ҫɾ����������')
                if weapon_name in weapon_list:
                    #ɾ��������remove(obj),pop(index),del weapon_list(index)
                    weapon_list.remove(weapon_name)
                    print(weapon_list)
                    break
                else:
                    print('����������������')
        else:
            print('�㶼û������������ʲô�����Ͽ칺��������')
        
    elif choice==4:
        print('��ǰ�����⣺{}����ǰ���coins:{}'.format(weapon_list,coins))
    elif choice==5:
        #���벻���ִ�Сд
        result=input('ȷ���˳���Ϸ��yes/no����\n')  
        answer=result.lower()     
        print('answer=',answer)
        if answer=='yes':
            break
    else:
        print('�������')