class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current_prefix = strs[0]
        max_len = len(current_prefix)

        for string in strs:
            for index, char in enumerate(current_prefix):
                if index >= len(string):
                    max_len = len(string)
                    current_prefix = current_prefix[:max_len]
                    break
                if char != string[index]:
                    max_len = index
                    current_prefix = current_prefix[:max_len]
        return current_prefix