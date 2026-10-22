class Solution:
    def reverse(self, x: int) -> int:
        to_string = str(x)
        negative = False
        if to_string[0] == "-":
            negative = True
            to_string = to_string[1:]
        actual_val = int(to_string[::-1])
        if negative and actual_val > 2**31:
            return 0
        if actual_val >= 2**31:
            return 0
        if negative:
            return -1 * actual_val
        return actual_val