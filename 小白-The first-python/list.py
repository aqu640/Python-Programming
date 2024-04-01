#####列表list用法#####
scores = [111, 100, 90, 80, 70]
people = ["伙食團","煮飯","電機","研究所"]
#print(scores[0])
#第一位 scores[0]
#倒數第一位 scores[-1]
  
  
print(people[2:])
  #取得第2位以後
phrase = "are you the one"
           #012345678
print(phrase[8:])
  #印出句子的第8位以後
  #phrase 短語 片語
print(1)
  
  
scores.append(60)
print(scores)
print(2)
  #列表最後加入60
  #append 附加
  
scores.extend(people)
print(scores)
  #list後面 加上一個list
  #extend 延伸
print(3)
  
scores.insert(0, 111)
print(scores)
  #0123 在第0位插入數字101
print(4)
  
scores.remove(70)
print(scores) 
print(5)
  #移除指定欄位

  
scores.pop()
print(scores)
print(6)
  #移除最後一位
  
  #scores.sort()
  #print(scores)
  #因為list後面加上list
  #執行會error
  
  #scores.reverse()
  #print(scores)
  #反轉
  
print(scores.count(111))
print(7)
  #數有幾個111
  
print(scores.index(90))
print(8)
  #搜尋90的位子
  
scores.clear()
print(scores)
print(9)
  #list淨空
  
  
  
  