#https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        m=nums[0]
        n=nums[0]
        for i in nums:
            if i>n:
                n=i
            if i<m:
                m=i

        return gcd(n,m)
        