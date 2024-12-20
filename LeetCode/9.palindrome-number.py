#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)[::-1]
        if temp == str(x):
            return True
        else:
            return False
# @lc code=end

