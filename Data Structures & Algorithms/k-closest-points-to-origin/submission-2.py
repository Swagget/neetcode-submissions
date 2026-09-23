class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # First create a list of distances from origin, with the same indices.
        self.distances = [point[0]**2 + point[1]**2 for point in points]
        self.indices = [ele for ele in range(len(points))]
        self.confirmed_close_points = []
        self.remaining_points = k
        self.k = k
        # Call quicksort then. Since order doesn't matter, that would be a great approach.
        self.quicksort(0,len(points)-1)

        to_return = [points[ele] for ele in self.confirmed_close_points]
        return to_return
    
    def quicksort(self, start, end): # Keep calling quicksort on the left side arrays. Discard the right side arrays unless left is small. End is a valid pivot.
        if start > end:
            return
        pivot_val = self.distances[end]
        divider = start
        for i in range(start, end):
            if self.distances[i] < pivot_val:
                self.swap(divider, i)
                divider += 1
        self.swap(end, divider) # Now divider is the exact index of the pivot

        if divider - start == self.remaining_points: # This is the points to the left of the pivot, as long as you don't include divider.
            self.confirm(start, divider-1)
            return True
        if divider - start == self.remaining_points - 1:
            self.confirm(start, divider)
            return True
        elif 1 + divider - start < self.remaining_points: # This points are confirmed, and we call quick sort on the larger than pivot points.
            self.confirm(start, divider)
            self.quicksort(divider + 1, end)
        elif divider - start > self.remaining_points: # We discard the larger points and continue to search among the smaller points
            self.quicksort(start, divider-1)

    def swap(self, a, b):
        self.distances[a], self.distances[b] = self.distances[b], self.distances[a]
        self.indices[a], self.indices[b] = self.indices[b], self.indices[a]

    def confirm(self, start, end): # This will add the points to the confirmed points and remove them from the remaining points, including start, and including end.
        for ele in range(start, end+1):
            self.confirmed_close_points.append(self.indices[ele])
            self.remaining_points -= 1
