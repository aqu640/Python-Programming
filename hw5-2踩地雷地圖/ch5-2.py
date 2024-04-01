"""
# Python程式設計 ch5-2
# Minesweeper踩地雷地圖
建立一個10X10的地圖，並利用for迴圈在地圖內隨機產生10個地雷
對每一個位子計算周邊八個位子內，總共有幾個地雷
https://www.askpython.com/python/examples/create-minesweeper-using-python

"""
# ==== 導入模組 ====
import random
import os
 
# ==== 踩地雷地圖的框框 ====
def print_minesweeper():
 
    global my_values   # 自己點選的格子 或旗子標記
    global n           # 地圖大小 
 
    print()
    print("\t\t\t=== MINESWEEPER ===\n")

    # ==== 印出 row (x軸) 的數字標籤 ====
    st = "   "
    for i in range(n):
        st = st + "     " + str(i + 1)
    print(st)   
    
    # ==== 印出 8個 ______ 當格子的線 ====
    for r in range(n):
        st = "     "
        if r == 0:
            for col in range(n):
                st = st + "______" 
            print(st)
            
        # ==== 印出 9個 | 當格子的線 ====
        st = "     "
        for col in range(n):
            st = st + "|     "
        print(st + "|")
         
        # 顯示 自己點選的格子 或旗子標記
        st = "  " + str(r + 1) + "  "
        for col in range(n):
            st = st + "|  " + str(my_values[r][col]) + "  "
        print(st + "|") 
        
        # ==== 印出 8個  |_____|當格子 ====
        st = "     "
        for col in range(n):
            st = st + "|_____"
        print(st + '|')
 
    print()

# ==== 設定地雷 ====
def set_mines():

    global numbers  # -1為地雷 其餘數字為周邊地雷數
    global mines    # 設定之地雷數目
    global n        # n x n 的地雷地圖
 
    # 追蹤設定了多少地雷數
    count = 0
    while count < mines: 
 
        val = random.randint(0, n*n -1) # 隨機產生
         
        r = val // n  # 產生地雷行列座標
        col = val % n
 
        if numbers[r][col] != -1: # 如果那格不是地雷
            count = count + 1     # 已設定地雷數+1
            numbers[r][col] = -1  # 將那格設定為地雷
 
# ==== 設定炸彈旁邊的數字 ====
def set_values():
 
    global numbers
    global n
 
    for r in range(n):
        for col in range(n):
 
            # [r][col] 座標有放地雷先跳過
            if numbers[r][col] == -1:
                continue
 
            # 上面那格有炸彈 炸彈數字+1   
            if r > 0 and numbers[r-1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # 檢查下方    
            if r < n-1  and numbers[r+1][col] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # 檢查左方
            if col > 0 and numbers[r][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # 檢查右方
            if col < n-1 and numbers[r][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # 檢查左上    
            if r > 0 and col > 0 and numbers[r-1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # 檢查右上
            if r > 0 and col < n-1 and numbers[r-1][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # 檢查左下 
            if r < n-1 and col > 0 and numbers[r+1][col-1] == -1:
                numbers[r][col] = numbers[r][col] + 1
            # 檢查右下
            if r < n-1 and col < n-1 and numbers[r+1][col+1] == -1:
                numbers[r][col] = numbers[r][col] + 1


# ==== 踩到0 把旁邊顯示出來 ====
def neighbor(r, col):
     
    global my_values
    global numbers
    global vis
 
    # If the cell already not visited
    if [r,col] not in vis:
 
        # Mark the cell visited
        vis.append([r,col])
 
        # 如果選取那格為0
        if numbers[r][col] == 0:
 
            # 把自己選的那格顯示出來
            my_values[r][col] = numbers[r][col]
 
            # 確認邊界 把旁邊的數字叫出來
            if r > 0:
                neighbor(r-1, col)
            if r < n-1:
                neighbor(r+1, col)
            if col > 0:
                neighbor(r, col-1)
            if col < n-1:
                neighbor(r, col+1)    
            if r > 0 and col > 0:
                neighbor(r-1, col-1)
            if r > 0 and col < n-1:
                neighbor(r-1, col+1)
            if r < n-1 and col > 0:
                neighbor(r+1, col-1)
            if r < n-1 and col < n-1:
                neighbor(r+1, col+1)  
 
        # 如果選取那格不為0 只顯示選取那格的結果(數字 or M)          
        if numbers[r][col] != 0:
                my_values[r][col] = numbers[r][col]


# ==== 清除用 ====
def clear():
    os.system("clear")      # os.system() 執行 shell 命令

# ==== 介紹輸入格式 ====
def Specification():
    print("<輸入格式:>")
    print("1. 選擇要踩的格子，輸入格式為 row column, 例 2 3")
    print("2. F 表示 flag, 輸入格式為 row column F , 例 2 3 F")


# ==== 結束遊戲前 檢查每一格 ====
def check_over():
    global my_values # 'M' 表示有地雷
    global n           # 地圖大小
    global mines       # 設定之地雷數
 
    # ==== 計數全部的格子 ====
    count = 0

    for r in range(n):
        for col in range(n):
 
            # 格子都有點選過 或 標記旗子
            if my_values[r][col] != ' ' and my_values[r][col] != 'F':
                count = count + 1
     
    if count == n * n - mines : # n x n - 地雷數
        return True # 地雷以外 都被選過 或標記旗子
    else:
        return False


# ==== 顯示地雷 M 的座標 ====               
def show_mines():
    global my_values # 'M' 表示有地雷
    global numbers # -1為地雷 其餘數字為周邊地雷數
    global n
 
    for r in range(n):
        for col in range(n):
            if numbers[r][col] == -1:     # 當陣列內值為-1 填入地雷
                my_values[r][col] = 'M'
 
 
if __name__ == "__main__": # Run這個.py文件時，if之下的code會啟動
 
    n = 10        # n x n 的地雷地圖
    mines = 10 # 設定地雷數
 
    # 全地圖座標 例如 [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    numbers = [  [0 for y in range(n)] for x in range(n) ] 
    
    # 空的座標 例如 [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    my_values = [  [' ' for y in range(n)] for x in range(n) ]
    # The positions that have been flagged
    flags = []  # 已放置的旗子座標
 
    
    set_mines() # 啟用 funtion 設定地雷
 
    set_values() # 啟用 funtion 設定炸彈旁邊的數字
 
         
    # ==== The GAME LOOP ====
    over = False
    while not over: # 沒輸 沒贏
        print_minesweeper() # 印出框框
        Specification()     # 介紹輸入格式
        # ==== 輸入 ====
        inp = input("\nEnter row number and column number = ").split()
 
        # ==== 輸入格式 ====
        if len(inp) == 2: # 標準輸入格式為 2 個數字
 
            # 輸入錯誤時 
            try: 
                val = list(map(int, inp))
            except ValueError:
                clear()
                print("Wrong input!")
                Specification()
                continue
 
        # ==== 標記旗子格式 ====
        elif len(inp) == 3: # 標準輸入為2個數字和 f(F)
            if inp[2] != 'F' and inp[2] != 'f':
                clear()
                print("=== 輸入錯誤 ===")
                Specification()
                continue
 
            # 輸入錯誤時  
            try:
                val = list(map(int, inp[:2]))
            except ValueError:
                clear()
                print("=== 輸入錯誤 ===")
                Specification()
                continue
 
            # input 不能大於n之邊界 也不能小於1 
            if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
                clear()
                print("=== 輸入錯誤 ===")
                Specification()
                continue
 
            # Get row and column number 電腦座標從0開始 所以要-1
            r = val[0]-1
            col = val[1]-1 
 
            # 已經放置旗子
            if [r, col] in flags:
                clear()
                print("=== 已經設定旗子 ===")
                continue
 
            # 已經顯示 或放置旗子
            if my_values[r][col] != ' ':
                clear()
                print("=== 已經知道數字 ===")
                continue
 
            # ==== 檢查旗子數目 ==== 
            if len(flags) < mines : # 旗子數 < 地雷數
                clear()
                print("=== 設定旗子 ===")
 
                # 將 flag append 為 list
                flags.append([r, col])
                 
                # 顯示設定 flag 那格為 F
                my_values[r][col] = 'F'
                continue
            else:
                clear()
                print("=== 旗子已經使用完 ===") # 旗子已經使用完
                continue    
 
        else: 
            clear()
            print("=== 輸入錯誤 ===")   
            Specification()
            continue
             
 
        # input 不能大於n之邊界 也不能小於1
        if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
            clear()
            print("=== 輸入錯誤 ===")
            Specification()
            continue
             
        # Get row and column number 電腦座標從0開始 所以要-1
        r = val[0]-1
        col = val[1]-1
 
        # 有放置旗子 亦可點選 
        if [r, col] in flags:
            flags.remove([r, col]) # 數字或地雷會取代旗子
 
        # 踩到有地雷那格 宣告失敗    
        if numbers[r][col] == -1:
            my_values[r][col] = 'M'
            show_mines()
            print_minesweeper()
            print("=== GAME OVER ===")
            over = True
            continue
 
        # 如果踩在附近地雷數為 0
        elif numbers[r][col] == 0:
            vis = []
            my_values[r][col] = '0'
            neighbor(r, col) # 把鄰居也顯示出來
 
        # 如果踩在附近地雷數至少1 
        else:   
            my_values[r][col] = numbers[r][col]
 
        # ==== 結束遊戲前檢查 ====
        if(check_over()):
            show_mines()         # 顯示地雷 M
            print_minesweeper()  # 顯示框框
            print("=== YOU WIN ===")
            over = True          # 已結束
            continue
        clear() 