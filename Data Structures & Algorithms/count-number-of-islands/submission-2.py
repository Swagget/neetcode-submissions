class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited_spots = set()
        num_islands = 0
        # columns = len(grid)
        # rows = len(grid[0])

        def dfs(i, j, grid, visited_spots):
            if min(i,j) < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == "0" or (i,j) in visited_spots:
                return None
            visited_spots.add((i,j))
            for ele in [(i-1,j), (i,j-1), (i+1,j), (i,j+1)]:
                dfs(ele[0], ele[1], grid, visited_spots)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited_spots and grid[i][j] == "1":
                    num_islands += 1
                    dfs(i, j, grid, visited_spots)
                

        return num_islands