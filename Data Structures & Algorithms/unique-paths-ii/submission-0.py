class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        cache = [[None for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]

        cache[-1][-1] = 1

        def traversal(i, j, cache, obstacleGrid):
            if i>= len(cache) or j >= len(cache[0]):
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if cache[i][j] is None:
                cache[i][j] = traversal(i+1, j, cache, obstacleGrid) + traversal(i, j+1, cache, obstacleGrid)
            return cache[i][j]

        return traversal(0, 0, cache, obstacleGrid)