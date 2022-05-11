#https://leetcode.com/problems/house-robber/
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0
        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
            
        
        # for i in range(len(nums)):
        #     if i % 2 == 0:
        #         sum1 = sum1 + nums[i]
        #         print(i)
        #     else:
        #         sum2 = sum2 + nums[i]
        #         print(i)
        #     return max(sum1, sum2)