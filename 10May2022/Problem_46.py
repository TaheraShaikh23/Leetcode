#https://leetcode.com/problems/permutations/
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
#         base case
        if (len(nums)== 1):
            # return [nums.copy()]
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            
            perms = self.permute(nums)
#             append the popped element
            
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
            
        return res
            
