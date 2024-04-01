"""
# LeetCode
# 1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

"""
class Solution():
    def __init__(self, nums, target):
        self.nums=nums 
        self.target=target
        
    def twoSum(self, nums, target):        
        d = {} # dictionary
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1
            print("d1=",d)
            if num2 in d:

                return [d[num2], i]
            d[num1] = i
            
sol = Solution([8,5], 13) # 類別 給值 命名sol
print(sol.twoSum([20,8,8,40,50,5,80], 13)) # sol 內的twoSum

"""
# print("num1=",num1)  =8
# print("num2= 13-5 =",num2)
"""