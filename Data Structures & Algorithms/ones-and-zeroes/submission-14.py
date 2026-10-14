class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        grid = [[[0] * (m+1) for _ in range(n+1)] for _2 in range(len(strs))]

        for k in range(len(strs)):
            for i in range(n+1):
                for j in range(m+1):
                        # for bin_str in strs:
                        num_0 = strs[k].count("0")
                        num_1 = strs[k].count("1") # This can be cached. Necessary for effeciency.
                        if num_1 <= i and num_0 <= j:
                            if k > 0:
                                grid[k][i][j] = max(grid[k-1][i][j], 1 + grid[k-1][i-num_1][j-num_0])
                            else:
                                grid[k][i][j] = 1
                        else:
                            grid[k][i][j] = grid[k-1][i][j]
        return grid[-1][n][m]