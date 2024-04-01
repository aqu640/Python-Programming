"""
# python ch5-3 猜數字2

"""
# ==== 導入模組 ====
import random
import itertools as it
count = 0

# ==== it.permutations() 對字串進行排列 所有可能的組合 ====
clist = [i for i in range(10)]
p = list(it.permutations(clist, 4)) # 從 5040 種可能開始
random.shuffle(p)                   # 將序列的所有元素随機排序
your_set = int(input("set four number let the computer guess:"))


try:
    while True :

        count += 1 # 用來記錄電腦猜幾次
        rlist = [] # 用來存放比對過後的 p 更新可能組合
        # 用dic 存放
        print(f"\n電腦第 {count} 次猜: {''.join ([str(i) for i in p [0]]) }")
        distinguish = input("輸入幾A幾B:")
        A = int(distinguish[0]) # 取出玩家輸入幾個 A
        B = int(distinguish[2]) # 取出玩家輸入幾個 B
        
        if A == 4:
            print("電腦答對了 共猜",count,"次")
            break
            
        # ==== 比對與之前猜測結果 ====
        for i in range(len(p)): # len(p) 為可能的組合數目
            count_A = 0
            count_B = 0
            #　p [0]　為電腦猜測
            for j in range(len( p [0])): # 固定第一位數 隨機比對
         
                 if p [i][j] in p [0]:
                     if j == p [0].index( p [i][j]): # .index()索引位置  
                         count_A += 1 
                     else:
                         count_B += 1 
                         
            # p [i] 為下一次的可能組合
            if  count_A == A and count_B == B:
                rlist.append( p [i])
        p = rlist # 存放比對過後的可能組合
        
        
except: 
    print("=== 玩家輸入有誤 ===") 
                 
