# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if target == nums[j] + nums[i]:
        #             return [i, j]
        dictNums={}
        for i in range (len(nums)):
            NumberB= nums[i]
            diff = target - NumberB
            if (diff) in dictNums:
                return(dictNums[diff], i)
            dictNums[NumberB]=i
# 2
# dictNum = {10:0,20:1,}
#  10
# numberB = 30
# [ 30 15 10 40 ] 40
# a + b = target
# Time complexity O(n2)
# Spcae complexity O(1)
# 0
# dictNum = {30:0, 25:1, }
#  [2, 0]
# numberB = 30
# [ 30 15 10 40 ] 40