class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        grid = [[""] * (len(str1) + 1) for ele in range(len(str2) + 1)]

        for i in range(len(str2) + 1):
            for j in range(len(str1) + 1):
                if i == j == 0:
                    continue
                min_str = False
                left_seq = False
                right_seq = False
                diag_seq = False
                if j > 0:
                    left_seq = grid[i][j-1] + str1[j-1]
                if i > 0:
                    right_seq = grid[i-1][j] + str2[i-1]
                if str1[j-1] == str2[i-1] and i > 0 and j > 0:
                    diag_seq = grid[i-1][j-1] + str1[j-1]
                for case in [left_seq, right_seq, diag_seq]:
                    if case:
                        if min_str:
                            if len(min_str) > len(case):
                                min_str = case
                        else:
                            min_str = case
                grid[i][j] = min_str
        return grid[-1][-1]