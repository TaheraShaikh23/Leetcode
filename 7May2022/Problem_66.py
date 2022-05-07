class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
#         r = len(digits) - 1
#         Numlist = [0,1,2,3,4,5,6,7,8]
#         if len(digits) == 0 and digits[r] == 9:
#             digits.append(1)
#             digits[r] = 0
#             # digits[r-1] = 1
#             print(digits)
            
        
#         if digits[r] == 9:
#             digits[r-1] += 1
#             digits[r] = 0
                
#         else:
#             digits[r] += 1
            
#         return digits
        
        digits = digits[::-1]
        carry, i = 1, 0
        
        while carry:
            if i < len(digits):
                if digits[i] == 9:
                    digits[i] = 0
                else:
                    digits[i] += 1
                    carry = 0
            else:
                digits.append(1)
                carry = 0
            i += 1
        return digits[::-1]