# -*- coding: utf-8 -*-
"""
For 迴圈
次方迴圈
"""
# for 變數 in 字串or列表:
#     重複執行的程式碼

# for letter in "小白你好":
#     print("letter=",letter)

# for num in [0,1,2,3]:
#     print("num=",num)

# for num in range(2,7):
#     print("num=",num)



def power(base,pow): # 基數 & 次方數
    result =1
    for index in range(pow):
        result =result *base
    return result
print("d=",power(4,2))

1* 4 *4


