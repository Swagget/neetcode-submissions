class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums is None:
            return 0
        current = nums[0]
        index = 1
        while index < len(nums):
            if current == nums[index]:
                del nums[index]
                continue
            current = nums[index]
            index += 1
        # for index, ele in enumerate(nums[1:]):
        #     if ele == current:
        #         del nums[index+1]
        return len(nums)