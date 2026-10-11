class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        reachable = {0:1}

        for i in nums:
            updated = {}
            for key, values in reachable.items():
                updated[key + i] = updated.get(key + i, 0) + values
                updated[key - i] = updated.get(key - i, 0) + values
            reachable = updated            
                
        return reachable.get(target, 0)