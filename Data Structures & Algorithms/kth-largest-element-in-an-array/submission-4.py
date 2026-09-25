class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        small_heap = []
        heapq.heapify(small_heap)
        for num in nums:
            heapq.heappush(small_heap, num)
            if len(small_heap) > k:
                heapq.heappop(small_heap)
        
        # while len(nums) > k:
        #     heapq.heappop(nums)
        return heapq.heappop(small_heap)