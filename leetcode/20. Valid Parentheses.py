"""
# leetcode
# 20. Valid Parentheses

"{[]}" => true

"""

class Solution(object):
    def isValid(self, s):
       
        lookup = {"(":")", "[":"]", "{":"}" } # 字典
        stack = [] # 堆疊
        for bracket in s:
            if bracket in lookup:
                stack.append( bracket )
                
            # 當pop() 最後一個 "(" 沒有對應 ")"
            elif len(stack) == 0 or lookup[stack.pop()] != bracket:

                return False 
            
        # s ="]" 不合if 所以 len(stack) == 0
        return len(stack) == 0

n = Solution("({}[])")
n.isValid("({}[])") 

"""
corresponding 對應
Valid         有效的 
parentheses   圓括號
Open brackets   => (
closing bracket =>  )
"""