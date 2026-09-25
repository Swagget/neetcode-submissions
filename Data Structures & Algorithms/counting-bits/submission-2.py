class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            temp = i
            temp_count = 0
            while temp > 0:
                if temp & 1 ==1:
                    temp_count += 1
                temp = temp >> 1
            ans.append(temp_count)
        return ans