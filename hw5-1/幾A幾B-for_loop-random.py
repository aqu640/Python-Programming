"""
# python ch5-1 猜數字遊戲

隨機產生4個不相同的0-9數字
再由使用者輸入4個數字
根據這2組數字，判斷
數字同時出現 & 位置相同，則獲得1個 A
數字同時出現 & 位置不相同，則獲得1個B
計算使用者輸入的數字能獲得幾A幾B？並顯示出來
"""

# ==== 導入 random 模組 ====
import random
answer = random.sample(range(0, 10), 4) # 隨機產生0~9 共4個數字 直接印出會是[1,2,3,4]

# ==== str.join( 元素串列 ) ====
number = "".join(map(str, answer))     # map 映射，是一對一對應 int轉換為 str 印出1234
print(number)                          # 先印出答案

A = B = n = 0                          # 設定 幾A、幾B、位置n 三個變數，預設值 0
guess = list(input('請輸入四個數字：'))  # 輸入數字 並透過 list 轉換成串列

# ==== 使用 for 迴圈 ====
for i in guess:                        # i 是輸入的數字號碼
    if int(guess[n]) == answer[n]:     # 從 n = 0 開始 依序比較 guess[0] ~ guess[3]
        A += 1                         # 如果內容物在位置上是相同的 將 A 增加 1
    else:
        if int(i) in answer:         # 如果答案裡有 輸入的數字(i)
            B += 1                   # 將 B 增加 1
    n += 1                           # 每判斷完一個 位置 guess[n] 將 n 增加 1
output = ','.join(guess).replace(',','') # 使用 .join() 將串列合併成字串

# ==== 使用 f-String 列印 ====
print(f'{output}: {A}A{B}B')             # 大括號填入字典的值 {A}A{B}B 等同 幾A幾B