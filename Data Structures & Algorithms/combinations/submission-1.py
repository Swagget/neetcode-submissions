class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        to_return = []
        current_set = []
        return self.recursive_helper(1, n, k, current_set, to_return)
        
    def recursive_helper(self, i, n, k, current_set, to_return):
        if len(current_set) == k:
            to_return.append(current_set.copy())
            return
        if i > n:
            return
        for iteration in range(i, n+1):
            current_set.append(iteration)
            self.recursive_helper(iteration + 1, n, k, current_set, to_return)
            current_set.pop()
        self.recursive_helper(iteration+1, n, k, current_set, to_return)
        return to_return