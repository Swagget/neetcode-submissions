class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_q = deque()
        fresh_count = 0
        minutes = 0
        grid_height = len(grid)
        grid_length = len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh_count += 1
                    continue
                if grid[i][j] == 2:
                    rotten_q.append((i,j))
                    continue
                    
        neighbors_delta = [[-1,0], [0,-1], [1,0], [0,1]]
        while fresh_count > 0 and len(rotten_q) > 0:
            fresh_rotten_this_minute = len(rotten_q)
            for _ in range(fresh_rotten_this_minute):
                rot_fruit = rotten_q.popleft()
                for neighbor in neighbors_delta:
                    i = rot_fruit[0] + neighbor[0]
                    j = rot_fruit[1] + neighbor[1]
                    if i < 0 or i == grid_height or j < 0 or j == grid_length or grid[i][j] != 1:
                        continue
                    fresh_count -= 1
                    grid[i][j] = 2
                    rotten_q.append((i,j))
            minutes += 1
        if fresh_count > 0:
            return -1
        return minutes