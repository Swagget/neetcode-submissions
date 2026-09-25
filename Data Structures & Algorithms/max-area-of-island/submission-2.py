class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        def dfs(i, j, grid, visited):
            if min(i,j) < 0 or i == len(grid) or j == len(grid[0]) or (i,j) in visited or grid[i][j] == 0:
                return 0
            new_found_area = 1
            visited.add((i,j))

            for ele in [(i-1,j), (i,j-1), (i+1,j), (i,j+1)]:
                new_found_area += dfs(ele[0], ele[1], grid, visited)

            return new_found_area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in visited or grid[i][j] == 0:
                    continue
                area = dfs(i, j, grid, visited)
                max_area = max(area, max_area)


        return max_area