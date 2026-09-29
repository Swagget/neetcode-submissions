class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_array_inclusive = [0 for ele in nums]
        prev_sum = 0
        for index, ele in enumerate(nums):
            self.prefix_array_inclusive[index] = prev_sum + ele
            prev_sum += ele

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix_array_inclusive[right] 
        return self.prefix_array_inclusive[right] - self.prefix_array_inclusive[left-1]            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)