class Solution:
    def maximumSwap(self, num: int) -> int:
        if num == 0:
            return 0
        nums = []

        while num != 0:
            nums.append(num%10)
            num //= 10
        
        nums.reverse()

        found_swap = False
        max_swap = -1
        for i in range(len(nums)):
            for j in range(len(nums)-1, i, -1):
                if nums[j] > nums[i]:
                    found_swap = True
                    if max_swap != -1:
                        if nums[j] > nums[max_swap]:
                            max_swap = j
                    else:
                        max_swap = j
            if found_swap:
                nums[i], nums[max_swap] = nums[max_swap], nums[i]
                #swap and break
                break
        to_return = 0
        # nums.reverse()

        for val in nums:
            to_return = to_return * 10
            to_return += val

        return to_return