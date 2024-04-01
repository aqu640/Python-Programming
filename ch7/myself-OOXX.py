# -*- coding: utf-8 -*-
"""
參考至 https://www.it145.com/9/92193.html
以及OOXX
"""
class into():
    # ==== 印一個只有 "." 的3X3 二維陣列  ====
    screen =[["." for i in range(3)] for j in range(3)]
    def place(self,x,y,person):
        global player, mark, over
        # ==== 定義範圍  ====
        try: 
            if into.screen[x][y]=="." and 0<=x<=2 and 0<=y<=2: # =< 會錯誤
                if player==2: # 2時，放xx
                    mark='X'
                else:
                    mark='O' # 5-2時，放xx
                into.screen[x][y]=mark
                over=game.determine(player)
                player=5-player
                into.show(self)
            # ==== 判斷錯誤 ====
            else:
                print("輸入位置已有棋子了，請重新輸入/n")
            
        except IndexError:
                print("座標有誤，請在範圍內/n")
    # ==== 判斷 ooxx 連線 ====
    def determine(self, person):
        global win
        win = person
        # ==== 沒有不等於空白，一開局就會結束 ====
        for row in range(3):
            if "." != into.screen[row][0] == into.screen[row][1] == into.screen[row][2]:
                return True
        # ==== 直線相同 ====
        for col in range(3):
            if "." != into.screen[0][col] == into.screen[1][col] == into.screen[2][col]:
                return True
        # ==== 斜線相同 ====
        if "." != into.screen[0][0] == into.screen[1][1] == into.screen[2][2]:
            return True
        # ==== 斜線相同 ====
        if "." != into.screen[2][0] == into.screen[1][1] == into.screen[0][2]:
            return True
    def show(self): # 顯示現在棋盤狀態
        for i in range(3):
            print(into.screen[i])
        print()
            
over=False # ==== 檢查是否結束
player=2   # 切換player 輪替mark
game=into() 
mark=''  


print(" 遊戲規則：\n","某玩家用OO，某玩家用XX\n",
      "雙方輪流放入自己的棋子\n",
      "若棋盤上有3顆相同的棋子\n",
      "在一行、一列或斜線上連線\n"
      " 則使用該棋子的玩家獲勝!\n")
# ==== 檢查是否結束的over 沒有成立則繼續

while not over: 
    print("player",player,":")
    lst=n=list(map(int, input("輸入座標，例如0 0 :").strip().split()))
    x1=int(lst[0])
    y1=int(lst[1])
    game.place(x1,y1,player)
if mark =='X':
    print("player",win," 用XX的人贏了") 
else :
    print("player",win," 用OO的人贏了") 