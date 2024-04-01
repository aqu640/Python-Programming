"""
# LeetCode
# 7. Reverse Integer

"""
class Solution(object):
    
    def __init__(self, x):
        self.x= x

    def reverse(self, x):
        a = abs(x) 
        num = 0 

        # abs return an absolute value of number
        # while迴圈 執行直到 a = 0
        while (a != 0):
            temp = a % 10
            print("a=",a)

            num = num*10 + temp
            print("temp=",temp)

            print("num=",num)
            a = a//10
            # a = int (a/10) 

    
        if x>0 and num < 2147483647:
            print("a=",a)
            return num
        elif x<0 and num < 2147483648:
            return -num
        else:
            return 0
            
num = Solution(12321) 
print("rev=",num.reverse(12321))


"""
# if x = 12321
# a = 1232, num = 1 
# temp = 2(餘數)
# num = 10+2 =12
# a = 123, num = 12 
# temp = 3(餘數)
# num = 120 +3
"""