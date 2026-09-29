class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        to_return = []

        left_product = []
        right_product =[] # This is last element, full thing will neeed to be reversed

        left_product_full = 1
        right_product_full = 1

        for index in range(len(nums)):
            left_product.append(left_product_full * nums[index])
            right_product.append(right_product_full * nums[(len(nums)-1) - index])
            left_product_full = left_product[-1]
            right_product_full = right_product[-1]

        right_product.reverse()

        to_return = [right_product[1]]

        for index in range(1,len(nums)-1):
            to_return.append(left_product[index-1] * right_product[index+1])
        to_return.append(left_product[-2])

        return to_return
        