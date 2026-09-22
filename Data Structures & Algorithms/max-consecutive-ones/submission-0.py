class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        counter = 0
        for ele in nums:
            if ele == 1:
                counter += 1
                max_ones = max(counter, max_ones)
            else:
                counter = 0

        return max_ones