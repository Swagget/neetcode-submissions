class Solution:
    def climbStairs(self, n: int) -> int:
        climb_cache = [0,1,2]
        for i in range(3,n + 1):
            climb_cache.append(climb_cache[i-1] + climb_cache[i-2])
        return climb_cache[n]