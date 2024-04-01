

#####清除指令cls#####

name = "先先真命"
print(name + "旺旺火星")
print("-")
print("火星旺旺\" 旺旺火星")
print("-")
# \"  右斜線加雙引號，\後面的"變字串一部份

print("火星旺旺\n旺旺火星")
# \n 是換行
print("-")
phrase = "Hello Mr.White"
         #01234 (第幾位)
         
         
#####如何使用函式#####           
print(phrase[0])
# 第0位
print(phrase.index("H"))
# H是第0位
print(phrase.index("l"))
# 有兩個l，在第2位第3位，回傳2
print(phrase.replace("Mr.White", "THE ONE")) 
#替換字串
print(phrase.lower())
print(phrase.lower().islower())
#lower字串變小寫
#upper字串變大寫
#islower判別是不是小寫 是回true 


#####如何使用數字#####
number = 8
print(number*10)
# 字串才是number = "8"
print(number%5)
# % 取餘數 8/5=1...3 

#####轉成字串#####
newnumber = 111
print("1+99=" + str(newnumber))
# str string 字串
# abs absolute 絕對值
print(pow(10, 2))
# pow power 10^2=100
print(max(1, 99, 111))
print(min(13, 888, 88888))
#最大最小 
print(round(87.5))
#4捨5入
#floor 地板 無條件捨去
#ceil 天花板 無條件進位
#sqrt 開根號




