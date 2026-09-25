class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_flag = set()
        for num in nums:
            if num in duplicate_flag:
                return True
            duplicate_flag.add(num)
        return False