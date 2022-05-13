#https://leetcode.com/problems/single-number/
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 # n ^ n = 0
        
        for n in nums:
            res = n ^ res
        return res
        
        