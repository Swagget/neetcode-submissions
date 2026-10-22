class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        start = 0
        end = 0
        max_width = 0

        max_right = deque([-1])
        max_right_temp = nums[-1]

        for ele in range(len(nums)-1, -1, -1):
            max_right_temp = max(max_right_temp, nums[ele])
            max_right.appendleft(max_right_temp)
        while end < len(nums):
            if start == end:
                end += 1
                continue
            if nums[end] >= nums[start] and max_width < end - start:
                max_width = end - start
                
            if max_right[end] >= nums[start]:
                end += 1
            else: start += 1
        return max_width