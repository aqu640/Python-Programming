# https://www.it145.com/9/92193.html
"""
# 重力四子棋 
模仿井字遊戲，完成8x8格的直立式四子棋
玩家輪流放棋子，只能決定放在哪一欄，棋子會從最底下往上堆疊
輸入8表示結束程式
如果能判斷是否獲勝或防止使用者輸入錯誤更佳，例如欄位輸入成非數字，或數目不在範圍內時請玩家重新輸入並警告輸入錯誤

"""
import sys 
import random

screen = [] # 棋盤列表
# ==== 初始空白棋盤 ====
def into():# 初始空白棋盤
    for i in range(6):     # 0~5
        list_width=[]
        for j in range(8): # 0~7
            list_width.append(' '+'|') # 框框放進空陣列
        screen.append(list_width)      # 框框放進空陣列

# ==== 列印棋盤 ====
def screen_print():
    print('',1,2,3,4,5,6,7,8,sep=' ')  # 棋盤列號
    for i in range(6):
        print('|',end='')
        for j in range(8):
            print(screen[i][j],end='') # 棋盤列表
        print('')
    print('——'*(9)) # 印出9條線當棋盤底部

# ==== 判斷輸贏 ====
def determine():
    # 判斷行
    for row in range(6): # 0~5 放進橫列裡
        for col in range(8-3): # 0~4 放進直行裡
            # ==== 陣列的行連續4個相同 且不等於空白====
            if screen[row][col][0]==screen[row][col+1][0]==screen[row][col+2][0]==screen[row][col+3][0] and screen[row][col][0]!=' ':
                return False
    #判斷列
    for row in range(6-3):
        for col in range(8):
            # ==== 陣列的列連續4個相同 且不等於空白 ====
            if screen[row][col][0]==screen[row+1][col][0]==screen[row+2][col][0]==screen[row+3][col][0] and screen[row][col][0]!=' ':
                return False
    #判斷斜線
    for row in range(6-3):
        for col in range(8-3):
          # ==== 陣列的斜線連續4個相同 ====
          if screen[row][col][0]==screen[row+1][col+1][0]==screen[row+2][col+2][0]==screen[row+3][col+3][0] and screen[row][col][0]!=' ':
              return False
          if col>=3:
              if screen[row][col][0] == screen[row+1][col-1][0] == screen[row+2][col-2][0] == screen[row+3][col-3][0] and screen[row][col][0] != ' ':
                  return False
    return True # 繼續放棋子

# ==== 電腦放棋子 ====
def com(): 
    global screen
    while True:
        coordinate = random.randint(0,7) # 0~7隨機取一
        flag = True
        high = 0
        for i in range(5,-1,-1): # 5~0
            if screen[i][coordinate][0] == ' ': # 棋盤有內容物
                high = i
                break
            if i == 0 and screen[i][coordinate][0] != ' ':
                flag = False
        if flag:
                screen[high][coordinate] = 'O' + '|' # flag= True 電腦放棋子
                break
    screen_print()

# ==== 玩家放棋子，只能決定放在哪一欄，棋子會從最底下往上堆疊 ====
def user():
    global screen
    while True:
        print(">>>輪到你了,請放X棋子,選擇列號(1-8): ",end='')
        coordinate = int(input())-1
        if coordinate not in range(7):
            print('結束程式，輸入須為1~7') # 輸入8 程式強制結束
            sys.exit() # 程式強制結束
        flag=True
        high=0
        for i in range(5,-1,-1):# 5~0
            if screen[i][coordinate][0] == ' ':
                high=i
                break
        if flag:
            screen[high][coordinate] = 'X' + '|'
        break
    screen_print()


if __name__ == '__main__':
    print(" 遊戲規則：電腦用O棋子，玩家用X棋子\n",
          "雙方輪流選擇列號放入自己的棋子\n",
          "若棋盤上有四顆相同型號的棋子\n",
          "在一行、一列或斜線上連線\n"
          " 則使用該棋子的玩家獲勝!\n")
    into()
    #screen_print()
    flag=True
    while determine() :      # determine為True 繼續執行電腦放棋子
        com()
        if not determine() : # 玩家放棋子
            flag=False
            break
        user()
    if flag:
        print('=== 你贏了 ===')
    else:
        print('=== 電腦贏了 ===')
        
