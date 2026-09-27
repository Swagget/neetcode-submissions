class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        start = 0
        end = 0
        max_val = nums[0]
        val = 0
        while start < len(nums) and end < len(nums):
            val += nums[end]
            max_val = max(val, max_val)
            if val <= 0:
                start = end + 1
                val = 0
            end += 1
        min_val = 0

        val = 0
        start = 0
        end = 0
        while start < len(nums) and end < len(nums):
            val += nums[end]
            min_val = min(val, min_val)
            if val >= 0:
                start = end + 1
                val = 0
            end += 1
        if sum(nums) == min_val:
            return max_val

        return max(max_val, sum(nums) - min_val)