class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for index in range(32):
            ans = ans << 1
            if n & 1 == 1:
                ans = ans | 1
            n = n >> 1
        return ans