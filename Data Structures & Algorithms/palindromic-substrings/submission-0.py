class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            l = r = i
            while l > -1 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1
            l = i
            r = i+1
            while l > -1 and r < len(s) and s[l] == s[r]:
                total += 1
                l -= 1
                r += 1
        return total