
# ==== 父類別 ====
class count:  
    def __init__(self, V, R, r_pi, Beta, VA):              
        self.IB = V/R
        self.V = V
        self.R = R
        self.r_pi = r_pi
        self.gm_1 = Beta /r_pi
        self.gm_2 = self.IB /0.025
        self.Beta = Beta 
        self.ro   = VA/self.IC
        self.IC   = self.Beta *self.IB
        self.Beta = Beta 
        self.r_e  = r_pi / (1 + self.Beta)

    def function_1(self):              
        print("IB= ",self.IB = V/R)
        print("IB= ",self.IB = V/R)
        print("IB= ",self.IB = V/R)
        print("IB= ",self.IB = V/R)


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
        

 

  







