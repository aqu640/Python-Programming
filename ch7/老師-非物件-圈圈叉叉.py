
tlist=[[0 for i in range(3)] for j in range(3)]
symbol=[' ','O','X']
delta=[[-1,-1],[-1,0],[0,-1],[-1,1]]
over=False
player=1
step=0
while not over and step<9:
    print("  0 1 2")
    for i in range(3):
        print(i,end=" ")
        for j in range(3):
            print(symbol[tlist[j][i]],end=" ")
        print()
    print("輪到 %s " %symbol[player],end="")
    location=input("請輸入座標：").split(",")
    x=int(location[0])
    y=int(location[1])
    if tlist[x][y]==0:
        tlist[x][y]=player
    else:
        print("輸入位置已有棋子了")
        continue
    #底下為判斷是否有人獲勝
    for dx,dy in delta:
        x1=x+dx
        y1=y+dy
        count=1            
        while x1>-1 and y1>-1 and y1<3:
            if tlist[x1][y1]==player:
                count+=1
                x1+=dx
                y1+=dy
            else:
                break
        x1=x-dx
        y1=y-dy
        while x1<3 and y1<3 and y1>-1:
            if tlist[x1][y1]==player:
                count+=1
                x1-=dx
                y1-=dy
            else:
                break
        if count>2:
            over=True
            break            
    player=3-player
    step+=1
print("  0 1 2")
for i in range(3):
    print(i,end=" ")
    for j in range(3):
        print(symbol[tlist[j][i]],end=" ")
    print()
if over:
    print("%s贏了" %symbol[3-player])
else:
    print("雙方平手")