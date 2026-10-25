class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if len(s) == 0:
            return ""
        i = 0
        j = -1
        for _ in range(int(len(s)/2)):
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        
        return s