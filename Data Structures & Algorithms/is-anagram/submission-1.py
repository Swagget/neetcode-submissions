class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}
        dict_2 = {}
        for ele in s:
            if ele in dict_1:
                dict_1[ele] += 1
            else:
                dict_1[ele] = 1
        for ele in t:
            if ele in dict_2:
                dict_2[ele] += 1
            else:
                dict_2[ele] = 1
        return dict_1 == dict_2
        # if len(dict_1.keys()) != len(dict_2.keys()):
        #     return False
        # for key in dict_1.keys():
        #     if key in dict_2:
        #         if dict_1[key] != dict_2[key]:
        #             return False
        #     else:
        #         return False
        # return True