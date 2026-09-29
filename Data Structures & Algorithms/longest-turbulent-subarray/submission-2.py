class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if arr is None:
            return 0
        if len(arr) == 1:
            return 1
        
        start = 0
        turbulent = "="
        max_len = 0
        for counter in range(1, len(arr)):
            if arr[counter] == arr[counter-1]:
                start = counter
                turbulent = "="
            elif arr[counter] > arr[counter-1] and turbulent in ["=", "<"]:
                turbulent = ">"
                
            elif arr[counter] < arr[counter-1] and turbulent in ["=", ">"]:
                turbulent = "<"
            
            else: 
                start = counter - 1
                if arr[counter] < arr[counter-1]: turbulet = "<"
                else: turbulet = ">"

                
            max_len = max(max_len, (counter - start) + 1)
        return max_len