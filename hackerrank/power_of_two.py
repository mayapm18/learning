#https://leetcode.com/problems/power-of-two/description/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n>0:
            while n > 1:
                if n % 2 != 0:
                    return False
                n = n // 2
            return True
        else:
           return False
