class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        to_return = []
        current_set = []
        sorted_nums = sorted(nums)
        return self.recursive_helper(0, sorted_nums, to_return, current_set)

    def recursive_helper(self, layer, sorted_nums, to_return, current_set):
        if layer == len(sorted_nums):
            to_return.append(current_set.copy())
            return 
        
        current_set.append(sorted_nums[layer]) # If yes
        self.recursive_helper(layer+1, sorted_nums, to_return, current_set)
        current_set.pop()

        # If no
        # Layer needs to move to where the next number is.
        while layer < len(sorted_nums)-1 and sorted_nums[layer] == sorted_nums[layer + 1]:
            layer += 1
        self.recursive_helper(layer+1, sorted_nums, to_return, current_set)

        return to_return