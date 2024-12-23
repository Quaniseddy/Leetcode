#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def insert_end(root,value):
        temp = ListNode()
        temp.val = value
        temp.next = root
        root = temp
        return root

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_number = []
        while l1.next != None:
            l1_number.append(str(l1.val))
            l1 = l1.next
        l1_number.append(str(l1.val))
        l1_number = ''.join(l1_number)

        l2_number = []
        while l2.next != None:
            l2_number.append(str(l2.val))
            l2 = l2.next
        l2_number.append(str(l2.val))
        l2_number = ''.join(l2_number)

        result = int(l1_number[::-1]) + int(l2_number[::-1])
        result = str(result)[::-1]
        
        root = None
        for i in range(len(result)-1,-1,-1):
            root = insert_end(root,int(result[i]))

        return root




# @lc code=end

