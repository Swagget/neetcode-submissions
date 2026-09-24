class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.to_return = []
        self.current_set = []
        self.nums = nums
        self.total_nums = len(nums)
        self.dfs(0)
        return self.to_return

    def dfs(self, index):
        if index == self.total_nums:
            self.to_return.append(self.current_set[:])
        else:
            # First no, then yes.
            self.dfs(index + 1)
            self.current_set.append(self.nums[index])
            self.dfs(index + 1)
            self.current_set.pop()
        return