#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
#         l, r = 0, len(matrix) - 1
        
#         while l < r:
#             for i in range(r - 1):
#                 top, bottom = l, r
            
#                 topleft = matrix[top][l + i]
            
#                 matrix[top][l + i] = matrix[bottom - i][l]
#                 matrix[bottom - i][l] = matrix[bottom][r - i]
#                 matrix[bottom][r - i] = matrix[top + i][r]
#                 matrix[top + i][r] = topleft
#             r -= 1
#             l += 1
        n = len(matrix)
        depth = n // 2
        for i in range(depth):
            rlen, opp = n - 2 * i - 1, n - 1 - i
            for j in range(rlen):
                temp = matrix[i][i+j]
                matrix[i][i+j] = matrix[opp-j][i]
                matrix[opp-j][i] = matrix[opp][opp-j]
                matrix[opp][opp-j] = matrix[i+j][opp]
                matrix[i+j][opp] = temp
            
            
        