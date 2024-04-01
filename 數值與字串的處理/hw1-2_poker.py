"""
# python ch3-1

隨機抽一張撲克牌，顯示其數字及花色
數字 23456789TJQKA
花色 ♠♥♦♣
♠T 表示 黑桃10
需印出 ♠T 中間不能有空白或逗號 
ord 順序
"""
# ==== 導入模組 ====
import random    
                    
# ==== random.choice (seq) ====     # 回傳一個隨機元素，以int數字顯示
x= random.choice([int(9824),         # spade   ord("♠")可得字元碼
                  int(9827),         # club    ord("♣")
                  int(9829),         # heart   ord("♥")
                  int(9830)])        # diamond ord("♦")

num = random.choice("23456789TJQKA") # 隨機抽出，字串內其中一個字
print('撲克牌:',chr(x)+num)          # chr() 將 Unicode 轉為字符
                                     # 用加號去連接，印出的字串就不會有空白




