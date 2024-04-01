##### 元組tuple #####
    #不可新增修改
    #scores = (111,100,90,80)
    #scores[0] = 30
    #更改第0位 會出錯
    #防止被修改 例如101的座標
    #data = (12345,67891)
    
##### 函式 #####


    
    #(1,99) 放進 (n1,n2)
    #再執行n1+n2
    #add 要放外面
    #同行不會執行
##### return順序 #####
   # print("1")
   # def two(r1,r2):
        #print("3")
       # return 111
       # print("5")
       # print(r1 +r2)
        #print("6")
   # print("2")     
   # print(two(1,99))
   # print("4")
    
##### return順序 #####

    def add(n1,n2): #1 定義空的add函式
        print(n1+n2) #3 印出1+99=100
        return 111 #4 有return 111會蓋掉原本(r1,r2)=(1,99)
        print(n1 +n2) #5  印出111

    print(add(1,99)) #2 呼叫add函式
    #2 先跳來有add這裡，把值帶入





