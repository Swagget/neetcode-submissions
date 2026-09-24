class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        max_k = max(piles)
        min_k = 1

        while min_k < max_k:
            mid_k = int(min_k + ((max_k - min_k)/2))
            hours = self.hours_needed(mid_k)
            if hours <= h: # We are good, eliminate all above, but keep this one
                max_k = mid_k 
            elif hours > h:
                min_k = mid_k + 1
        if min_k == max_k:
            return min_k
        
        
    def hours_needed(self, k):
        return -sum([-ele // k for ele in self.piles])