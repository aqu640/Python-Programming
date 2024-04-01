"""
# leetcode
# 21. Merge Two Sorted Lists

list1 = [1,2,4]
list2 = [1,3,4]

Output: [1,1,2,3,4,4]

Merge the two lists in a one sorted list.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next
class Solution(object):
    def mergeTwoLists(self, L1, L2):
        curr = dummy = ListNode(0) # curr current dummy 虛擬
        
        # val有文字有數字 只轉數字
        while  L1 and  L2:
            if  L1.val <  L2.val:  
                     curr.next = L1 # next 返回下一個輸入行
                     L1 = L1.next
            else:
                curr.next = L2
                L2=  L2.next
            curr =  curr.next
        curr.next =  L1 or  L2 # L1結束 接 L2
        return dummy.next
    
n=  ListNode( [1,2,4], [1,3,4])
print(n.val)
print(n.next)

        
        
        
        
        
        
        

