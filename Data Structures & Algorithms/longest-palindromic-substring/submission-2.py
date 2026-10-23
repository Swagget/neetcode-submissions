class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        start = 0

        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if max_len < (r - l)+1:
                    max_len = (r - l)+1
                    start = l
                l -= 1
                r += 1
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if max_len < (r - l)+1:
                    max_len = (r - l)+1
                    start = l
                l -= 1
                r += 1
        return s[start:(start + max_len)]