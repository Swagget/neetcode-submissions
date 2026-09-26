class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_left = 0
        max_right = len(heights) - 1

        max_volume = (max_right - max_left) * min(heights[max_right], heights[max_left])

        right_counter = max_right
        left_counter = max_left

        while right_counter > left_counter:
            current_volume = (right_counter - left_counter) * min(heights[right_counter], heights[left_counter])
            if current_volume > max_volume:
                max_volume = (right_counter - left_counter) * min(heights[right_counter], heights[left_counter])
                max_left = left_counter
                max_right = right_counter
            if heights[right_counter] < heights[left_counter]:
                right_counter -= 1
                continue
            elif heights[right_counter] > heights[left_counter]:
                left_counter += 1
                continue
            else:
                right_counter -= 1
                left_counter += 1
                
        return max_volume