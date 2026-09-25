class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_indices = {}
        for index, ele in enumerate(nums):
            if target-ele in seen_indices:
                return [seen_indices[target-ele], index]
            seen_indices[ele] = index