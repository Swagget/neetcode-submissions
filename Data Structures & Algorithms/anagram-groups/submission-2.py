class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def generate_key(string):
            char_counts = {}
            for char in string:
                if char in char_counts:
                    char_counts[char] += 1
                else:
                    char_counts[char] = 1
            sorted_keys = sorted(char_counts.keys()) # Check syntax

            to_return = []

            for key in sorted_keys:
                to_return.append(f"{key}:{char_counts[key]}")


            return " ".join(to_return)
        
        anagrams_hash = {}

        for string in strs:
            key = generate_key(string)
            if key in anagrams_hash:
                anagrams_hash[key].append(string)
            else:
                anagrams_hash[key] = [string]
        
        to_return = []
        for key in anagrams_hash.keys():
            to_append = []
            for string in anagrams_hash[key]:
                to_append.append(string)
            to_return.append(to_append)

        return to_return