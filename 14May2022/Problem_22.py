#https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #only add open pranthesis if open < n
#         only add a closing paranthesis if closed < open
#  valid IIF open == closed == n
        
        stack= []
        res = []
        
        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()
                
            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()
                
        backtrack(0, 0)
        return res