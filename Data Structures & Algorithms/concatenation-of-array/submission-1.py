class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums[:]
        for ele in nums:
            ans.append(ele)
        return ans