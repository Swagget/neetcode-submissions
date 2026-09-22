class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ele in s:
            if ele in ['(', '{', '[']:
                stack.append(ele)
            elif len(stack) > 0:
                if ele == ')':
                    if stack[-1] == '(':
                        del stack[-1]
                    else:
                        return False
                if ele == '}':
                    if stack[-1] == '{':
                        del stack[-1]
                    else:
                        return False
                if ele == ']':
                    if stack[-1] == '[':
                        del stack[-1]
                    else:
                        return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False