# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 06:54:05 2021

Advanced Calculator capable of infinite addition and subtraction

@author: kyleb
"""
addSubArr = []
output=0
funct = input("Input an equation with only addition and subtraction: ")


"Create array which holds both the index and type of operation to perform in lists. Then change original input to use commas as delimiters"
i = 0
j = 0
for char in funct:
    if char == "+":
        if j != 0 and addSubArr[j-1] == [i-1, "+"]:
            addSubArr[j-1] = [i, "+"]
            funct= funct[:i] + funct[i+1:]
        elif j != 0 and addSubArr[j-1] == [i-1, "-"]:
            addSubArr[j-1] = [i,"-"]
            funct = funct[:i] + funct[i+1:]
        else:     
            addSubArr.append([i, "+"])
            funct = funct[:i] + "," + funct[i+1:]
            j = j+1
    elif char == "-":
        if j != 0 and addSubArr[j-1] == [i-1,"+"]:
            addSubArr[j-1] = [i, "-"]
            funct = funct[:i] + funct[i+1:]
        elif j != 0 and addSubArr[j-1] == [i-1, "-"]:
            addSubArr[j-1] = [i, "+"]
            funct = funct[:i] + funct[i+1:]
        else:
            addSubArr.append([i, "-"])
            funct = funct[:i] + "," + funct[i+1:]
            j = j+1
    i = i+1
numArr = funct.split(",")

"Implement lists as stacks, utilizing FIFO order to interate through values"
for num in numArr:
    while 0 < len(numArr)-1:
        if addSubArr[0][1] == "+":
            numArr[0] = int(numArr.pop(0)) + int(numArr[0])
            addSubArr.pop(0)
        elif addSubArr[0][1] == "-":
            numArr[0] = int(numArr.pop(0)) - int(numArr[0])
            addSubArr.pop(0)
for num in numArr:
    print(num)