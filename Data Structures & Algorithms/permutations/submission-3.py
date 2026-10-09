class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        to_return = []
        
        
        return self.recursive_helper(0, to_return, nums)

    def recursive_helper(self, i, to_return, nums):
        if i == len(nums):
            return [[]]
        
        all_perms_from_next = self.recursive_helper(i+1, to_return, nums)

        to_return = []

        for perm in all_perms_from_next:
            inserting_char = nums[i]
            for position in range(0, len(perm) + 1):
                to_return.append(perm[:position] + [inserting_char] + perm[position:])
        
        return to_return