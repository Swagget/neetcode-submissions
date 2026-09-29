class Solution:
    def trap(self, height: List[int]) -> int:
        if height is None:
            return 0
        max_left = height[0]
        max_right = height[-1]
        total_volume = 0
        if max_left <= max_right:
            move = "left"
        else:
            move = "right"
        right_counter = len(height)-1
        left_counter = 0

        while left_counter != right_counter:
            if move == "left":
                left_counter += 1
                max_left = max(max_left, height[left_counter])
                empty_space = max_left - height[left_counter]
                total_volume += empty_space
            if move == "right":
                right_counter -= 1
                max_right = max(max_right, height[right_counter])
                empty_space = max_right - height[right_counter]
                total_volume += empty_space
            if max_left <= max_right:
                move = "left"
            else:
                move = "right"
        return total_volume