class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        val_dict = {0:0, 1:0, 2:0}
        for ele in nums:
            val_dict[ele] += 1

        keys = [0,1,2]
        current_key = 0
        for ele in range(len(nums)):
            while val_dict[current_key] == 0:
                current_key += 1
            nums[ele] = current_key
            val_dict[current_key] -= 1
        