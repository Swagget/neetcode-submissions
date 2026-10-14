class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        grid = [[None] * (amount + 1) for _ in range(len(coins))]

        for i in range(len(grid)):
            grid[i][0] = 1
        for j in range(1, len(grid[0])):
            if j % coins[0] == 0:
                grid[0][j] = 1
            else:
                grid[0][j] = 0
        
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                take = 0
                if j >= coins[i]:
                    take = grid[i][j-coins[i]]
                dont_take = grid[i-1][j]
                grid[i][j] = take + dont_take
        return grid[-1][-1]