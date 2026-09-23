class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        start = 0
        end = len(nums) - 1
        while start < end:
            mid = int(start + ((end - start)/2))
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                end = mid - 1
            if nums[mid] < target:
                start = mid + 1
        if nums[start] != target:
            return -1
        else:
            return start