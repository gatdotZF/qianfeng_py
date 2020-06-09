#! usr/bin/env python
#encoding=utf-8

txt=r'r.txt'
new_list=[]
with open(txt,'r+') as file0:
    lines=file0.read()
    print(lines)
    elemnt_list=lines.split()
    print(elemnt_list)
    for elemnt in elemnt_list:
        elemnt=int(elemnt,16)
        print(elemnt)
        file0.write(str(elemnt)+' ')
        new_list.append(str(elemnt))
file0.close()