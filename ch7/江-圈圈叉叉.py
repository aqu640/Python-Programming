# -*- coding: utf-8 -*-
"""
Created on Wed May 31 16:35:04 2023

@author: r
"""

#create a class for the chess game, which includes all the variables and function
class chess():
    board = [['_']*3 for i in range(3)] #create a empty board
        
    def place(self,x,y,person): #define a function for placing the chess at the assigned coordinate
        global state, player, mark, over
        
        try: #define a exceptional handling for fear that the program exit when facing some idex problem 
            if chess.board[x][y]=='_' and 0<=x<3 and 0<=y<3:
                if player==1:
                    mark='X'
                else:
                    mark='O'
                chess.board[x][y]=mark
                over=game.winning_move(mark,player)
                player=3-player
                chess.show(self)
            else:
                print("Plesase eneter a valid coordinate!")
                print()
            
        except IndexError:
                print("Plesase eneter a valid coordinate!")
                print()
        
        
    def show(self): #print out the chess board
        for i in range(3):
            print(chess.board[i])
        print()
        
    #判斷是否連線四顆棋子成功
    def winning_move(self, piece, person):
        global win
        win = person
        # 橫向判斷，colomn因邊界只要算到5，從第一列到第八列掃描確認
        for r in range(3):
            if chess.board[r][0] == piece and chess.board[r][1] == piece and chess.board[r][2]:
                return True

        # 直向判斷，從第一列到第八列掃描確認，row從下往上數只要掃到4個，
        for c in range(3):
            if chess.board[0][c] == piece and chess.board[1][c] == piece and chess.board[2][c] == piece:
                return True

        # 左上到右下的對角線判斷，colomn因邊界只要算到5，再過去不會有左上到右下的機會
        
        if chess.board[0][0] == piece and chess.board[1][1] == piece and chess.board[2][2] == piece:
            return True

        # 左下到右上的對角線判斷，colomn因邊界只要算到5，再過去不會有左下到右上的機會
        if chess.board[2][0] == piece and chess.board[1][1] == piece and chess.board[0][2] == piece:
            return True
        
        
        
        
over=False #set a variable to keep the operation and when to finishe
player=1 # defalt start with player1
game=chess() #define a game as chess object
mark='' #blank mark char, so the program will decide which mark should be later by switching between player1 and 2
print("Board Game Start...") # welcome slogan
while not over: #what should do as loop
    print("player",player,":")
    lst=n=list(map(int, input("Please enter a location (seperated by a space) :").strip().split()))
    game.place(lst[0],lst[1],player)

print("player",win,"wins!!!") #when the game is over, then print who wins the game

