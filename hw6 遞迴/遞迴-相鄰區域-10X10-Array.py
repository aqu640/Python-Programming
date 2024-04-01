"""
利用遞迴尋找相鄰區域
在一個10X10的陣列中，裡面填滿了一堆0跟1
請輸入任一座標(x,y)，如果[x][y]的值為0
則將[x][y]的值改為X，並將與之相鄰的0都
改為X，其餘不相鄰的0不更動
如果[x][y]的值為1，則不處理，程式結束
"""
import random
# ==== 10X10的陣列的框框 ====
def print_minesweeper():
    global my_values   # 自己點選的格子
    global n           # 格子大小 n =10 為 10X10 
    print()
    print("\t\t\t=== 找相鄰區域 ===\n")

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
         
        # 顯示 自己點選的格子
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

# ==== 設定之數字1數目 ====
def set_mines():

    global numbers  # 1 
    global mines    # 設定之數字1數目
    global n        # n x n 的地圖
 
    # 追蹤設定了多少數字1
    count = 0
    while count < mines: 
        val = random.randint(0, n*n -1) # 隨機產生       
        r = val // n  # 產生行列座標
        col = val % n
        
        if numbers[r][col] != 1: # 如果那格不是 1
            count = count + 1     # 已設定數 +1
            numbers[r][col] = 1  # 將那格設定為 1
            my_values[r][col] = numbers[r][col]
        
# ==== 設定 1 旁邊的數字 ====
def set_values():
 
    global numbers
    global n
 
    for r in range(n):
        for col in range(n):

            # [r][col] 座標有 1 先跳過
            if numbers[r][col] == 1:
                my_values[r][col] = numbers[r][col]
                continue
            if numbers[r][col] == 0: # 如果那格不是 1
                my_values[r][col] = numbers[r][col]
                continue

# ==== 踩到0 把旁邊顯示出來 ====
def neighbor(r, col):
     
    global my_values
    global numbers
    global vis
 
    # If the cell already not visited
    if [r,col] not in vis:
 
        # Mark the cell visited
        vis.append([r,col])
 
        # 如果選取那格為0 改成 X
        if numbers[r][col] == 0:
            my_values[r][col] = 'X'
            numbers[r][col] = my_values[r][col]
 
            # 確認邊界 把旁邊的數字叫出來
            if r > 0:
                neighbor(r-1, col)
            if r < n-1:
                neighbor(r+1, col)
            if col > 0:
                neighbor(r, col-1)
            if col < n-1:
                neighbor(r, col+1)    
            # if r > 0 and col > 0:
            #     neighbor(r-1, col-1)
            # if r > 0 and col < n-1:
            #     neighbor(r-1, col+1)
            # if r < n-1 and col > 0:
            #     neighbor(r+1, col-1)
            # if r < n-1 and col < n-1:
            #     neighbor(r+1, col+1)  
 
        # 如果選取那格不為0 只顯示選取那格的結果(數字)          
        if numbers[r][col] != 0:
                my_values[r][col] = numbers[r][col]

# ==== 介紹輸入格式 ====
def Specification():
    print("1. 選擇要踩的格子，輸入格式為 row column, 例 2 3")

# ==== 顯示 1 的座標 ====               
def show_mines():
    global my_values # 空的座標
    global numbers   # 全地圖座標
    global n
 
    for r in range(n):
        for col in range(n):
            if numbers[r][col] == 1:     # 當陣列內值為1 填入1
                my_values[r][col] = '1'
 
if __name__ == "__main__": # Run這個文件時，if之下的code會啟動
    n = 10        # n x n 的地圖
    mines = random.randint(55, 66) # 設定 數字1的個數
 
    # 全地圖座標 例如 [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    numbers = [  [0 for y in range(n)] for x in range(n) ] 
    
    # 空的座標 例如 [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    my_values = [  [' ' for y in range(n)] for x in range(n) ]
 
    set_mines() # 啟用 funtion 設定 1
    set_values() # 啟用 funtion 設定數字1旁邊的數字
        
    # ==== The GAME LOOP ====
    over = False
    while not over: # 尚未結束
        print_minesweeper() # 印出框框
        Specification()     # 介紹輸入格式
        # ==== 輸入 ====
        inp = input("\n請輸入任一座標(x,y) = ").split()
 
        # ==== 輸入格式 ====
        if len(inp) == 2: # 標準輸入格式為 2 個數字
            try: 
                val = list(map(int, inp))
            except ValueError:
                print("輸入錯誤!")
                Specification()
                continue         
 
        # input 不能大於n之邊界 也不能小於1
        if val[0] > n or val[0] < 1 or val[1] > n or val[1] < 1:
            # clear()
            print("=== 輸入錯誤 ===")
            Specification()
            continue
             
        # 設定 row column 電腦座標從0開始 所以要-1
        r = val[0]-1
        col = val[1]-1

        # 踩到有數字1那格 宣告結束  
        if numbers[r][col] == 1:
            my_values[r][col] = '1'
            show_mines()
            print_minesweeper()
            print("=== [x][y]的值為1，不處理，程式結束 ===")
            print("=== end ===")
            over = True
            continue
 
        # ==== 如果踩在 0 ====      
        else:     
            vis = []            
            neighbor(r, col) # 把鄰居顯示出來 改成X
            my_values[r][col] = 'X'
            numbers[r][col] = my_values[r][col]