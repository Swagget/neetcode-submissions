class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for num in nums_set:
            if num-1 not in nums_set:
                current_length = 1
                while num + current_length in nums_set:
                    current_length += 1
                max_len = max(max_len, current_length)

        return max_len