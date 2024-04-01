# -*- coding: utf-8 -*-
"""
Created on Thu May 11 13:28:43 2023

@author: r
"""

import random #匯入模組

# 建立10x10的空地圖
lst = [['0']*10 for i in range(10)]

#隨機生成1, 製造有0、1的地圖
mines = random.sample([(i, j) for i in range(10) for j in range(10)], 70)
for i, j in mines:
    lst[i][j] = '1'

# 顯示地圖
print(lst)

#定義遞迴函數
def change(x,y):
    global lst #將地圖宣告為global函數以便做每次的更改
    if x<0 or x>=10 or y<0 or y>=10 or lst[x][y]=='1' or lst[x][y]=='X' :
        return x,y #當已經到達邊境或不需要更改的位置時，把位置傳回
    lst[x][y]='X' #將當下的位子改成X
    x1,y1=change(x, y) #傳回給新的變數，所以從新的x,y出發去判斷
    change(x1-1, y1)
    change(x1+1, y1)
    change(x1, y1-1)
    change(x1, y1+1)
    return lst

#輸入x,y，並呼叫遞迴函數
x=int(input('x:'))
y=int(input('y:'))
print(change(x, y))
