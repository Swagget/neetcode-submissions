class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = []

        for start in range(0, len(nums)-2):
            if start > 0 and nums[start] == nums[start - 1]:
                continue
            i = start + 1
            j = len(nums) - 1
            while i < j:
                total_sum = nums[start] + nums[i] + nums[j]
                if total_sum == 0:
                    answers.append([nums[start], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                    continue
                if total_sum < 0:
                    i += 1
                    continue
                if total_sum > 0:
                    j -= 1
                    continue
        return answers