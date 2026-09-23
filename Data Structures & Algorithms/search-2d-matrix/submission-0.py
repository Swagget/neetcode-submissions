class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Easy solution is just to flatten it out and then perform normal binary search. 
        # Now I don't want to actually flatten it out, since that would take n time. 
        # So I'm just going to do a normal binary search, but with the indices translated to matrix form.
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False
        start = 0
        end = (m*n)-1 # Indices
        while start < end:
            mid = int(start + ((end-start)/2))
            x = int(mid/n)
            y = mid % n
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                start = mid + 1
            elif matrix[x][y] > target:
                end = mid - 1
        # what if start is greater than end? That w
        x = int(start/n)
        y = start % n
        if matrix[x][y] == target:
            return True
        return False