class Solution:
    def numSquares(self, n: int) -> int:
        min_nums = [i for i in range(n+1)]

        for i in range(1, n+1):
            for s in range(1, int(i ** 0.5) + 1):
                if i-(s ** 2) >= 0:
                    min_nums[i] = min(min_nums[i], 1 + min_nums[i - (s ** 2)])
        return min_nums[n]