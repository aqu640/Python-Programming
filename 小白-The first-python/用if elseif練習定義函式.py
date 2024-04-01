# -*- coding: utf-8 -*-
"""
如果你考111分
ʕ•ᴥ•ʔ
或是如果你考100分以上
ʕ·ᴥ·ʔ 
或是如果你考90分以上
ʕˊ·ᴥ0ˋʔ 
否則
ˁ˙˟˙ˀ
"""

scores = 1                     # 1個 = , 把111帶入scores
running = True                 # 2個 == , 判斷左&右的值有沒有相等
eating = False                 # False要大寫
if scores == 111 and running :
    print("ʕ•ᴥ•ʔ")
elif scores >= 100 or eating:
    print("ʕ•ᴥ•ʔ")
elif scores >= 88:
    print("ʕ•ᴥ•ʔ")
else:
    print("ˁ˙˟˙ˀ")             # 最後else要加 " : " 
"""
用if elseif練習定義函式
"""
def max_num(num1,num2,num3):   # def definition 定義函數
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num3 and num2>=num1:
        return num2
    else:
        return num3
print(max(1, 8, 13))


        
    
    


    



