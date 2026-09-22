class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        top = -1
        for ele in operations:
            if ele == '+':
                stack.append(stack[top] + stack[top-1])
                top += 1
            elif ele == 'D':
                stack.append(stack[top]*2)
                top += 1
            elif ele == 'C':
                del stack[top]
                top -= 1
            else:
                stack.append(int(ele))
                top += 1
            # print("operation", ele, "stack", stack)
        # total = 0
        # print(stack)
        # for ele in stack:
        #     total += ele
        return sum(stack)