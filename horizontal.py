# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 09:04:36 2020

@author: Faraz
"""
matrix = []

def extractSubMatrix(
    matrix, 
    rowStartIdx, rowEndIdx,
    colStartIdx, colEndIdx):

    result = [
        x[ colStartIdx : colEndIdx ]
        for x in matrix[ rowStartIdx : rowEndIdx ]
    ]

    return result



def text_line(histogram_Array):
    indexs = []
    i = 0
    while i < len(histogram_Array):
        if histogram_Array[i] == 0:
            indexs.append(i)
        i = i + 1
    print(indexs)
    j = 0
    h = 0
    updated_start = 0
    start = -1 
    end = -1
    while(j < len(indexs)):
        if updated_start != 0:
            start = updated_start
        if(j == 0):
            if indexs[j] == 0:
                start = indexs[j] + 1
            else:
                start = 0
                end = indexs[j] - 1
        else:
            end = indexs[j] - 1
            updated_start = indexs[j] + 1
        j = j + 1
        if(start != -1 and end != -1 and start != end):
            h = h + (end - start + 1)
           # width = 5
            r = 0
            subMatrix = extractSubMatrix(matrix,
                start, h+1, 
                0, width)
            h = h + 1
            print("SubMatrix:")
            for array in subMatrix: 
                print(array)
        
      
            

    

def calculate_HorizontalHistogram(array):
    
    horizontal_Histogram = []
    for i in array:
        count = 0
        for black in i:
            if black == 0:
                count = count + 1
        horizontal_Histogram.append(count)
    return horizontal_Histogram


    
    

def arr2D():
    
    global matrix
    m = int(input('number of rows, m = '))
    n = int(input('number of columns, n = '))
    global width 
    width = n 
    for i in range(0,m):
        matrix.append([])
        for j in range(0,n):
            input_user = int(input(f'enter pixel value for {i,j} in array{i} position '))
            matrix[i].append(input_user)
    print(matrix)
    List = calculate_HorizontalHistogram(matrix)
    print(List)
    text_line(List)

arr2D()



    
    