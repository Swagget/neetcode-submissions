class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        if len(s)<=2:
            return 0
        
        pal_count = [0,0,1]
        hash_set = {} # character to list of occurences
        palindromes = set()

        for index, char in enumerate(s[:3]):
            if char in hash_set:
                hash_set[char].append(index)
            else:
                hash_set[char] = [index]
        if s[0] == s[2]:
            palindromes.add(s[:3])

        # start iterating from 4th char
        

        for index, char in enumerate(s[3:]):
            true_index = index+3
            if char in hash_set:
                hash_set[char].append(true_index)
            else:
                hash_set[char] = [true_index]
            new_palindromes = 0
            if len(hash_set[char]) == 1: # middle check and add
                continue
            last_position = hash_set[char][-2]
            curr_position = true_index
            for middle_ele_index in range(last_position+1, curr_position):
                available_palindrome = f"{char}{s[middle_ele_index]}{char}"
                if available_palindrome not in palindromes:
                    palindromes.add(available_palindrome)
                    new_palindromes += 1

            if len(hash_set[char]) == 3: # middle check and add
                new_palindromes += 1
                palindromes.add(f"{char}{char}{char}")
            
            pal_count.append(pal_count[-1]+new_palindromes)
    
        return len(palindromes)