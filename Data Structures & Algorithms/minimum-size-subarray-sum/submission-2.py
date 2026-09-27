class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        current_val = nums[0]
        min_length = None
        while right < len(nums):
            if current_val >= target:
                length = (right - left) + 1
                if min_length is None:
                    min_length = length
                else:
                    min_length = min(length, min_length)
                current_val -= nums[left]
                left += 1
                if right < left and left < len(nums):
                    right = left
                    current_val = nums[right]
            else:
                right += 1
                if right < len(nums):
                    current_val += nums[right]

        if min_length is not None:
            return min_length
        return 0