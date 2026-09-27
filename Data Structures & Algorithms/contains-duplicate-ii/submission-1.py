class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        seen = set()
        for i in range(k):
            if i >= len(nums):
                return False
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        
        for end in range(k, len(nums)):
            if nums[end] in seen:
                return True
            seen.add(nums[end])
            seen.remove(nums[end-k])
        return False