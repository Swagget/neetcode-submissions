class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = [[None for _ in range(n+1)] for _ in range(m+1)]
        cache[m-1][n-1] = 1
        for ele in range(n+1):
            cache[-1][ele] = 0
        for ele in range(m+1):
            cache[ele][-1] = 0
        
        def traversal(i, j, cache):
            if cache[i][j] is None:
                cache[i][j] = traversal(i+1, j, cache) + traversal(i, j+1, cache)
            return cache[i][j]
        
        return traversal(0,0, cache)