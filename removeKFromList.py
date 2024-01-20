'''
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and an integer k, remove all elements from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
solution(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
solution(l, k) = [1, 2, 3, 4, 5, 6, 7].
Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer k

An integer.

Guaranteed constraints:
-1000 ≤ k ≤ 1000.

[output] linkedlist.integer

Return l with all the values equal to k removed.
'''
# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def solution(l, k):
    if l:
        current = l
        nextNode = current.next
        while(nextNode):
            if current.value == k and current == l:
                l = current.next
                current = l
                nextNode = current.next
            elif nextNode.value == k:
                current.next = nextNode.next
                nextNode = nextNode.next
            else:
                current = current.next
                nextNode = current.next 
    
    if l and l.value == k:
        return []
    else:
        return l
        
    
