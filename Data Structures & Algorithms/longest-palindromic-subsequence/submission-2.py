class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        grid = [[0] * (len(s) + 1) for ele in range(len(s) + 1)]

        source = s[:]
        target = source[::-1]

        grid[0][0] = 0

        for i in range(1, len(s) + 1):
            for j in range(1, len(s) + 1):
                if source[i - 1] == target[j - 1]:
                    grid[i][j] = grid[i-1][j-1] + 1
                grid[i][j] = max(grid[i][j], grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]