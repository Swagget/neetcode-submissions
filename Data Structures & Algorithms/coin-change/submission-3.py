class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        grid = [[-1] * (amount + 1) for _ in coins] # y-axis = index of coin available, x-axis = amount searched for. Grid contains minimum coins needed. If not possible grid contains -1.

        for ele in range(amount + 1):
            if ele % coins[0] == 0:
                grid[0][ele] = ele / coins[0]
        
        for i in range(1, len(coins)):
            for j in range(amount + 1):
                grid[i][j] = grid[i-1][j] # Up value is default
                if j >= coins[i] and grid[i][j-coins[i]] != -1:
                    if grid[i][j] == -1: # If the up is impossible and we can pick the current coin. Then we must.
                        grid[i][j] = 1+grid[i][j-coins[i]]
                    else:
                        grid[i][j] = min(1 + grid[i][j-coins[i]], grid[i][j])
        return int(grid[-1][-1])