class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n == 1:
            return bool(1)
        elif n % 2 == 0:
            while n > 1:#initiate a loop that repeats a block of code as long as a condition is true
                n = n // 2
            if n == 1:
                return bool(1)
            else:
                return bool(0)
        else:
           return bool(0)
