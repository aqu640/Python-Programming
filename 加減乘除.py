# -*- coding: utf-8 -*-
"""
建立一個物件，在初始時給定兩個數字
如果初始設定時沒有給初始值，則兩個數字預設值為1
物件提供四個函數分別將兩數相加、減、乘、除
除法函數需要判斷以避免除0
"""
class function:
    def __init__(self, a=1, b=1):
        self.num1 = a
        self.num2 = b
    def add(self):
        return self.num1 + self.num2
    
    # def subtract(self):
    #     return self.num1 - self.num2
    
    # def multiplicate(self):
    #     return self.num1 * self.num2
    
    # def divise(self):
    #     if self.num2 == 0 :
    #         return self.num1 / self.num2
    #     else :
    #         print("non")
     
calculate = function(1,99)
print( calculate.add() )

    




