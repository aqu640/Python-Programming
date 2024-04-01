"""
# python ch5-3 猜數字2

由玩家選不重複的 4個0-9數字，讓電腦猜數字，
當電腦猜某答案時，由玩家輸入?A ?B，
電腦根據之前猜測結果，重新猜下一個答案，直到猜對為止
提示：
先建立所有可能的答案組合的 list，總共有5040（10*9*8*7）個
從 clist 裡面隨機挑一個答案出來，比對與之前猜測結果 rlist 裡的資料
如果跟之前的猜測結果相同，則輸出這個數字
如果玩家回答4A0B，遊戲結束
如果 clist 取完還沒結束，則顯示玩家輸入有誤，並將 rlist 顯示出來

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
        print("=== 輸入範例: 2A1B ===")
        distinguish = input("輸入幾A幾B:")
        A = int(distinguish[0]) # 取出玩家輸入幾個 A
        B = int(distinguish[2]) # 取出玩家輸入幾個 B
        
        if distinguish[1] != A and distinguish[3] != B:
            print("格式錯誤")
            count -= 1 # 電腦猜測次數不更動  
            break

 
        if A == 4:
            print("電腦答對了 共猜",count,"次",
                  "\n答案為: ",your_set)
            break
        if A+B > 4 or A+B < 0:
            print("=== 輸入錯誤 ===")
            count -= 1 # 電腦猜測次數不更動  
            
        # ==== 比對與之前猜測結果 ====
        for i in range(len(p)): # len(p) 為可能的組合數目
            count_A = 0
            count_B = 0
            #　p [0]　為電腦猜測
            for j in range(len( p [0])): # 固定第一位數 隨機比對
         
                 if p [i][j] in p [0]:
                     if j == p [0].index( p [i][j]): # .index()索引位置  
                         count_A += 1 # 數字對 &位置一樣 A+1
                     else:
                         count_B += 1 # 數字對 &位置不對 B+1
                         
            # p [i] 為下一次的可能組合
            if  count_A == A and count_B == B:
                rlist.append( p [i])
        p = rlist # 存放比對過後的可能組合
        
#  如果可能組合都沒有答案，則為AB判斷有誤
#  如果輸入重複，則輸入錯誤
except: 
    print("=== 玩家輸入有誤 ===") 
                 
