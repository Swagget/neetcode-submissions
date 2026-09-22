class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest_to_right = None
        temp_saving = None
        for index in range(len(arr)-1, -1, -1):
            if greatest_to_right is None:
                greatest_to_right = arr[index] # Need to copy this by value instead of by reference somehow.
                arr[index] = -1
                continue
            temp_saving = arr[index]
            arr[index] = greatest_to_right
            greatest_to_right = max(temp_saving, greatest_to_right)
            # if arr[index] > greatest_to_right:
            #     next_greatest_to_right = arr[index]
            # arr[index] = greatest_to_right
        return arr