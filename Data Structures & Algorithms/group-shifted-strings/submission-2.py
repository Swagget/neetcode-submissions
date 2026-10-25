class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        int_lists = []
        
        for string in strings:
            numberified_string = ["0"]
            first_char = string[0]
            if len(string)>1:
                for char in string[1:]:
                    to_append = ord(char) - ord(first_char)
                    if to_append < 0:
                        to_append += 26
                    numberified_string.append(str(to_append))
            
            int_lists.append(numberified_string)
        
        dict_int_lists_to_indices = {}

        for index, int_list in enumerate(int_lists):
            key = " ".join(int_list)
            current_values_attached = dict_int_lists_to_indices.get(key, []) + [index]
            dict_int_lists_to_indices[key] = current_values_attached
        
        to_return = []

        for key in dict_int_lists_to_indices.keys():
            to_append = []
            for index in dict_int_lists_to_indices[key]:
                to_append.append(strings[index])
            to_return.append(to_append)
        
        return to_return