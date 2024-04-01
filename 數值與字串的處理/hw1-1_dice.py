"""
# python ch3-1

投擲4顆骰子，每顆骰子出現點數為隨機1-6的數字
Unicode 9856-9861
chr(9856)
由下列可得 Unicode
print(ord("⚀"),ord("⚁"),ord("⚂"),ord("⚃"),ord("⚄"),ord("⚅")) 
"""
# ==== 導入模組 ====
import random

# ==== random.randint(a, b) ====
a = random.randint(9856,9861)      # 回傳一個隨機整數 N，使得 a <= N <= b
b = random.randint(9856,9861)      # 從9856~9861隨機取一個數
c = random.randint(9856,9861)
d = random.randint(9856,9861)

print("投擲4顆骰子，每顆骰子出現點數為")
print(chr(a),chr(b),chr(c),chr(d))    # 轉為chr印出

"""
我有試著用迴圈寫，取出四個
但list沒辦法轉成ord去列印
就用簡單列印

s =[]
while (len(s)<4):                 # len() 傳回字串的長度
    x = random.randint(9856,9861)
    if x not in s:
        (s.append(x))
print((s))
"""



