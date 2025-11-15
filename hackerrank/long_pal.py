#https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        r_word = ''#reverse word
        for char in s:
            r_word = char + r_word
        pal = ''
        n = len(s)
        if n==2:
            if s==r_word:
                pal = s
            else:
                pal = s[1]
        else:
            for i in range(n):
                k = i
                j = i
                if s[k] == r_word[j]: 
                    pal = pal + s[i] 
                
        return pal
