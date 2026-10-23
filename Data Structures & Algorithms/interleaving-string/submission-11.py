class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        grid = [[False] * (len(s2)+1) for ele in range(len(s1)+1)]
        grid[0][0] = True

        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == j == 0:
                    continue
                top = i > 0 and s1[i-1] == s3[i+j-1] and grid[i-1][j]
                left = j > 0 and s2[j-1] == s3[i+j-1] and grid[i][j-1]
                grid[i][j] = top or left
        if grid[-1][-1]:
            return True
        return False