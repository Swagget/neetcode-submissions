class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        k_grid = grid.copy()

        k_grid = [[-1] * len(grid[0]) for _ in range(len(grid))]

        frontier = []
        heapq.heapify(frontier)
        heapq.heappush(frontier, [grid[0][0], 0, 0])


        reached = {}

        t = 0

        while len(frontier) > 0:
            if frontier[0][0] > t:
                t += 1
                continue
            available_pos = heapq.heappop(frontier)[1:]
            

            if k_grid[available_pos[0]][available_pos[1]] != -1:
                continue
            k_grid[available_pos[0]][available_pos[1]] = t
            
            # Add surrounding tiles to frontier
            for surrounding_delta in [[-1, 0], [0, -1], [1, 0], [0,1]]:
                next_i = available_pos[0] + surrounding_delta[0]
                next_j = available_pos[1] + surrounding_delta[1]
                if next_i < 0 or next_j < 0 or next_i >= len(grid) or next_j >= len(grid[0]):
                    continue
                if k_grid[next_i][next_j] == -1:
                    heapq.heappush(frontier, [grid[next_i][next_j], next_i, next_j])

            # Check if the last position is reached
            if k_grid[len(grid)-1][len(grid[0])-1] != -1:
                return t