class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_sum = nums[0]
        sum_current_subarray = 0
        for right in range(len(nums)):
            if sum_current_subarray < 0:
                left = right
                sum_current_subarray = 0
            sum_current_subarray += nums[right]
            if sum_current_subarray > max_sum:
                max_sum = sum_current_subarray
        return max_sum