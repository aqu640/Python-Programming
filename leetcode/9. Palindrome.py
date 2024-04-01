"""
# LeetCode
# 9. Palindrome

"""
class Solution(object):
    def __init__(self, x):
        self.x=x
    def isPalindrome(self, x):
        a = abs(x) 
        num = 0 

        while (a != 0):
            temp = a % 10
            num = num*10 + temp
            a = a//10 
            # a = int (a/10) 
    
        if num ==x and x>=0 and num < 2147483647:
            return True
            return num
        elif num !=x and x<0 and num < 2147483648:
            return False
        else:
            return False
        
n = Solution(0)
print(n.isPalindrome(0))

# x = 0
# x = 10
# x = 121


