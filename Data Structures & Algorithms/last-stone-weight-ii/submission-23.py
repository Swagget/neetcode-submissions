class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        sum_stones = sum(stones)
        grid = [[0]*(int(sum_stones/2) + 1) for _ in range(len(stones))]

        for j in range((int(sum_stones/2) + 1)):
            if stones[0] <= j:
                grid[0][j] = j-stones[0]
            else:
                grid[0][j] = j
# This subset that I'm picking has to strictly be the smaller one. That's totally fine.
        for i in range(1,len(stones)):
            for j in range((int(sum_stones/2) + 1)):
                if stones[i] <= j:
                    remaining_target = j - stones[i]

                    grid[i][j] = min(grid[i-1][remaining_target], grid[i-1][j])
                # If I pick the stone
                else:
                    grid[i][j] = grid[i-1][j]
                # If I don't pick the stone
        gap =  grid[-1][-1]

        smaller_subset = int(sum_stones/2) - gap

        return sum_stones - (2*smaller_subset)