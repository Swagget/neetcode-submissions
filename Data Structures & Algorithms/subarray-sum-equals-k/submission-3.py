class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_hash = {0:1}
        prefix_value = 0
        total_found = 0
        for end in range(len(nums)):
            current_value = prefix_value + nums[end]
            total_found += prefix_hash.get(current_value - k, 0)
            prefix_hash[current_value] = prefix_hash.get(prefix_value + nums[end], 0) + 1
            prefix_value = current_value
        return total_found