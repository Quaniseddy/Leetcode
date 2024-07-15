#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        result = {}
        n = len(nums)

        for i in range(n):
            remain = target - nums[i]
            if remain in result:
                return [result[remain],i]
            result[nums[i]] = i
        
        return []
        
# @lc code=end

