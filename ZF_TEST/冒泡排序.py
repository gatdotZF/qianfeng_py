#! /usr/bin/env python
#coding=GB18030
def bubbleSort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
arr=[64,34,25,12,22,11,90,22]

bubbleSort(arr)
print("排序后的数组：{}".format(arr))
print(set(arr))
