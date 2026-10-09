class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digits_to_chars = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        to_return = [char for char in digits_to_chars[digits[0]]]
        for number in digits[1:]:
            temp = []
            for ele in to_return:
                for char in digits_to_chars[number]:
                    temp.append(ele+char)

            to_return = temp
        return to_return