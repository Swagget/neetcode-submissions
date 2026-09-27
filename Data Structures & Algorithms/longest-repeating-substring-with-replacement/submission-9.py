class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        # end = 0
        count = {}
        # max_f = 0
        max_len = 0
        max_char = s[0]
        for end in range(0, len(s)):
            # Adding end to the string
            # max_f = max(max_f, count.get(s[end], 0))
            count[s[end]] = 1 + count.get(s[end], 0)
            if count[s[end]] > count[max_char]:
                max_char = s[end]
            max_characters = count[max_char]
            replacements = 1 + end - start - max_characters
            
            if replacements <= k:
                max_len =  1 + end - start
            else:
                count[s[start]] -= 1
                start += 1
        return max_len