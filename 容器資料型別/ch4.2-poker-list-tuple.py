"""
# python ch4-2

將編號 0-51 的撲克牌分成4等分，並以4個 list 傳回。
4個 list 以 tuple 型式傳回 
主程式接收到4組牌，必須以4個 list 來接收資料
主程式接收到4組資料後，先排序然後再分別列印出來
"""
import random as rd       # 縮寫
a = list (range(0,52,1))  # ( 起始, 結束52-1, 間隔 )

x = rd.shuffle (a)      # 將 list 內的資料打散    
                        # 不傳回值 可印a 不可印x

# ==== 隨機分成4分，用4個 list 儲存 ====
length = len (a)                     # 回傳的字符串的長度
n = 4
step = int (length/n)                # step = 13，4*13=52

for i in range ( 0, length, step ) : # 從 0~52 隨機選 13次
    b = tuple (a[ i: i+ step ])      # 將 list 轉為 tuple (可以增減不可修改)
    y = sorted (b)                   # i = 0 ~ 0+ step排序
    print (y)

