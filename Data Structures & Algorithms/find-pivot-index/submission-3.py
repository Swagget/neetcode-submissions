class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum = []
        prev_sum = 0
        for ele in nums:
            prefix_sum.append(ele + prev_sum)
            prev_sum += ele
        total = sum(nums)
        if total - nums[0] == 0:
            return 0

        for index in range(1, len(prefix_sum)-1):
            if prefix_sum[index - 1] == total - prefix_sum[index]:
                return index
            
        if total - nums[-1] == 0:
            return len(nums)-1

        return -1