class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        grid = [[None for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

        def recursive(i, j, grid, text1, text2):
            if i >= len(text1) or j >= len(text2):
                return 0
            if text1[i] == text2[j]:
                grid[i][j] = 1+recursive(i+1, j+1, grid, text1, text2)
                return grid[i][j]
            if grid[i][j] is None:
                grid[i][j] = max(recursive(i+1, j, grid, text1, text2), recursive(i, j+1, grid, text1, text2))
            return grid[i][j]
        
        return recursive(0, 0, grid, text1, text2)