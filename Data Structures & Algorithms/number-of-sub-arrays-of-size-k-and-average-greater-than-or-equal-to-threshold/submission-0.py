class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        
        current_val = 0
        total_cross_threshold = 0
        true_threshold = threshold * k
        flag = True
        for start in range(0, len(arr)-k+1):
            if flag:
                flag = False
                current_val = sum(arr[:k])
            else:
                current_val -= arr[start-1]
                current_val += arr[start + k - 1]
            if current_val >= true_threshold:
                total_cross_threshold += 1
        return total_cross_threshold