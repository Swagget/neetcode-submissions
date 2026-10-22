class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current_candidate = None
        candidate_count = 0
        for ele in nums:
            if candidate_count == 0:
                current_candidate = ele
                candidate_count += 1
            elif ele == current_candidate:
                candidate_count += 1
            else:
                candidate_count -=1
        return current_candidate