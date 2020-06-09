#! /usr/bin/env python
#coding=GB18030
import random
print('*'*15,'王者荣耀','*'*15)
print('\t欢迎来到王者荣耀游戏')
role=input('请选择人物：\n 1.鲁班\n 2.后羿\n 3.李白\n 4.孙尚香\n 5.貂蝉\n 6.诸葛亮\n')
coins=1000
weapon_list=[]
print('欢迎{}来到王者荣耀，当前金币是{}'.format(role,coins))
while True:
    choice=int(input('请选择：\n 1.购买武器\n 2.打仗\n 3.删除武器\n 4.查看武器\n 5.退出游戏\n'))
    if choice==1:
#         pass
        print('\t欢迎来到武器库')
        weapons=[['98K',500],['屠龙刀','400'],['樱花枪','600'],['喷火枪',1000]]
        for weapon in weapons:
            print(weapon[0],weapon[1],sep='   ')  #中间间隔多个空格
        #输入要购买的武器名称
        weapon_name=input('请输入要购买的武器名：')
        if weapon_name not in weapon_list:
            for weapon in weapons:
                if weapon_name == weapon[0]:
                    if coins >=int(weapon[1]):
                        coins-=int(weapon[1])
                        weapon_list.append(weapon[0])
                        break
                    else:
                        print('金币不足，请赶紧挣金币')
                else:
                    print('输入武器名称错误！')
         
    elif choice==2:
        #假设你拥有多个武器
        print('进入战场……')
        if len(weapon_list)>0:
        #选择武器
            print('{}拥有的武器如下：{}'.format(role,weapon_list))
            for weapon in weapon_list:
                print(weapon)
            while True:
                weapon_name=input('请选择：')
                if weapon_name in weapon_list:
                    #进入战争状态，默认跟张飞
                    ran1=random.randint(1,20)  #张飞
                    ran2=random.randint(1,20)  #role
                    if ran1>ran2:
                        print('此局对战：张飞胜利！')
                    elif ran1==ran2:
                        print('此局对战：平局！')
                    else:
                        print('此局对战：{}胜利'.format(role))
                        coins+=200
                    break   
                else:
                    print('选择的武器不存在，请重新选择')
        else:
            print('还没有购买武器，赶快使用金币购买武器吧！')        
    elif choice==3:
        #查询武器库
        print('当前武器库：{}'.format(weapon_list))
        if len(weapon_list)>0:
            for weapon in weapon_list:
                print(weapon)
            while True:
                weapon_name=input('请输入要删除的武器：')
                if weapon_name in weapon_list:
                    #删除武器：remove(obj),pop(index),del weapon_list(index)
                    weapon_list.remove(weapon_name)
                    print(weapon_list)
                    break
                else:
                    print('武器名称输入有误！')
        else:
            print('你都没有武器，还扔什么……赶快购买武器！')
        
    elif choice==4:
        print('当前武器库：{}，当前金币coins:{}'.format(weapon_list,coins))
    elif choice==5:
        #输入不区分大小写
        result=input('确定退出游戏（yes/no）？\n')  
        answer=result.lower()     
        print('answer=',answer)
        if answer=='yes':
            break
    else:
        print('输入错误！')