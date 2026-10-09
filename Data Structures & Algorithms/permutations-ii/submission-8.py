class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        to_return = []
        if len(nums) == 0:
            return [[]]
        return self.recursive_helper(0, nums)
    
    def recursive_helper(self, i, nums):
        if i == len(nums):
            return [[]]
        
        all_permutations_beyond = self.recursive_helper(i+1, nums)
        to_return = []
        for permutation in all_permutations_beyond:
            char_inserting = nums[i]
            position = 0
            while position <= len(permutation):
                to_return.append(permutation[:position] + [char_inserting] + permutation[position:])
                if position < len(permutation) and permutation[position] == char_inserting:
                    break
                position += 1
        
        return to_return