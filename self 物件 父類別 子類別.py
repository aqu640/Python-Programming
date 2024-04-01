# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 17:14:04 2023

@author: r
"""
# ==== 父類別 ====
class count:  
    def __init__(self,n, L):              
        self.side = L
        self.num = n
    def function_1(self):              
        print(self.side*self.num)

# 輸出邊長
# c =count(4,5)            
# c.function_1()

# ==== 子類別  ==== 
class Area(count): # 繼承count  用 L&4 取代 L&n
    def function_2(self):              
        print("function_2 =", self.side*self.side)
    def __init__(self,L): 
        self.side = L
        self.num = 4
# 輸出面積
# c = Area(5)
# c.function_2() 
# 
# 如不指定self.num = 4 
# c = Area(4,5)

# ==== 子類別 ==== 
import numpy as np
class tri(count):
    
    def triangle(self): 
        print("Area =",self.side*self.side * 0.25 * (3** 0.5))
        print("Area_2 =",self.side*self.side * 0.25 * (np.sqrt(3)  )  ) # sqrt() 開根號

        # (3** 0.5) = 根號3 (根號3/4*L^2)
# 輸出三角形面積
# c = tri(3,10)
# c.triangle()  
        

 

  







