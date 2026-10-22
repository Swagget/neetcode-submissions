class Solution:
    def isPalindrome(self, x: int) -> bool:
        to_string = str(x)
        for ele in range(len(to_string)):
            if to_string[ele] != to_string[len(to_string) - (ele+1)]:
                return False
        return True