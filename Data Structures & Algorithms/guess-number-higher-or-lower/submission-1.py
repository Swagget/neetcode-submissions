# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        minimum = 1
        maximum = n
        my_guess = 1

        while minimum != maximum:
            my_guess = int((maximum + minimum)/2)
            answer = guess(my_guess)
            if answer == -1:
                maximum = my_guess - 1
            elif answer == 1:
                minimum = my_guess + 1
            else:
                return my_guess
        my_guess = minimum
        return my_guess