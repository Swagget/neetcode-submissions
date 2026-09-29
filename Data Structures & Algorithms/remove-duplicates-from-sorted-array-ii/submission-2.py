class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        if len(nums) < 3:
            if len(nums) == 1:
                return 1
            if nums[0] == nums[1]:
                return 1
            return 2
        unique = 1
        if nums[0] != nums[1]:
            unique += 1
        k = 2
        while k <= len(nums)-1:
            if nums[k] == nums[k-1] and nums[k] == nums[k-2]:
                del nums[k]
                continue
            else:
                unique += 1
            k += 1
        return k