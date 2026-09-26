class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_sub = 0
        temp_counter = 0
        end = 0
        start = 0
        while end != len(s):
            if end == start:
                temp_counter = 1
                hash_table = {s[start] : start}
                end += 1
                max_sub = max(max_sub, temp_counter)
                continue
            elif s[end] in hash_table:
                for i in range(start, hash_table[s[end]]):
                    del hash_table[s[i]]
                start = hash_table[s[end]] + 1
                hash_table[s[end]] = end
                temp_counter = end - start + 1
            else:
                temp_counter += 1
                hash_table[s[end]] = end
                max_sub = max(max_sub, temp_counter)
            end += 1
        return max_sub