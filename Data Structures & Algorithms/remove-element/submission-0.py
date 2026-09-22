class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        total_removed = 0
        for index, element in enumerate(nums):
            if element == val:
                total_removed += 1
                continue
            nums[index - total_removed] = nums[index]
        return len(nums) - total_removed