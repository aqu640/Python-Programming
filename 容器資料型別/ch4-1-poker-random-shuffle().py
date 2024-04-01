"""
# python ch4-1

將 52 張撲克牌編號成 0-51
隨機分成4分，分別用4個list儲存 ( random 套件裡的 shuffle( ) 將資料打散 )
並將編號由小到大排序顯示出來 ( sorted( )可對 list 的資料做排序)
""" 
# ==== 導入 random 模組 ====
import random as rd      
a = list (range(0,52,1))  # ( 起始, 結束52-1, 間隔 )
x = rd.shuffle (a)        # 將 list 內的資料打散    
                          # 不傳回值 可印a 不可印x

# ==== 隨機分成4分，用4個 list 儲存 ====
length = len(a)                      # 回傳的字符串的長度
n = 4
step = int ( length / n )            # step = 13，4*13=52

for i in range ( 0, length, step ) : # 從 0~52 隨機選 13次
    y = sorted ( a[ i: i+ step ] )   # i = 0 ~ 0+ step排序
    print (y)

