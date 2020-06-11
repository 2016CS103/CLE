# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 14:45:34 2020

@author: Faraz
"""

array = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 1, 1, 0, 1, 1, 1],[1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],[1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
         [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 0, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],[1, 1, 1, 0, 1, 0, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
         [1, 1, 0, 0, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


def crop_Above(array):
    count = 0
    for i in array:
        if any(elem is 0 for elem in i):
            break
        else:
            array.pop(count)
            count = count + 1
    return array[count:len(array)]

croped = crop_Above(array)

print(croped)

def crop_Below(array):
    k = - 1
    while(k > -len(array)):
        if any(elem is 0 for elem in array[k]):
            break
        else:
            array.pop(k)
            k = k - 1
    return array[-len(array): k+1]
    
below = crop_Below(croped)    

print(below)


def crop_left(array):
    for i in range(0, 10):
        count = 0
        for j in range(0, 14):
            if array[j][i] == 0:
                return array
            if array[j][i] == 1:
                count = count + 1
        if count == 14:
            k = 0
            m = 0
            while(m < len(array)):
                array[m].pop(k)
                m = m + 1
    return array
left = crop_left(below)
print(left)

def crop_Right(array):
    i = -1
    while(i > -10):
   # for i in range(-1, -10):
        count = 0
        for j in range(0, 14):
            if array[j][i] == 0:
                return array
            if array[j][i] == 1:
                count = count + 1
        if count == 14:
            k = -1
            m = 0
            while(m < len(array)):
                array[m].pop(k)
                m = m + 1
    return array
Right = crop_Right(left)
print(Right)






