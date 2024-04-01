"""
# LeetCode
# 1. Two Sum

# num1 + num2 = target 
https://ithelp.ithome.com.tw/articles/10269246

此題有  class Solution(object):
    須再學習
"""

def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        print("i=",i)
        num1 = nums[i]
        num2 = target - num1 # 5有重複
        if num2 in d: 
            print("num2=",num2)
            print("num1=",num1)

            return [d[num2], i]
        d[num1] = i
        print("d[num1]=",i)

twoSum([3,8,8,2,5,4], 13)

# <法二>
# def twoSum( nums, target):
#     i = 0
#     j = len(nums) - 1
    
#     while (nums[i] + nums[j] != target):
#         if (nums[i] + nums[j] > target):
#             j = j - 1
#         else:
#             i = i + 1
#             # print("i=",i,"j=",j)    
#     return [i, j]

# twoSum([2,3,4,5,8,8], 13)
# 此法需排序
