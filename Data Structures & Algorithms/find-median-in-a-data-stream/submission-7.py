import heapq

class MedianFinder:

    def __init__(self):
        self.small_max_heap = []
        heapq.heapify(self.small_max_heap) # by default everything is a min heap
        self.big_min_heap = []
        heapq.heapify(self.big_min_heap)
        self.even = True
        

    def addNum(self, num: int) -> None:
        # Add to either larger heap or smaller heap. Depending on position relative to median. If smaller than median then add to small heap. else add to big heap

        current_median = self.findMedian()
        if self.even:
            self.even = False
        else:
            self.even = True
        
        if num > current_median: # Add to big heap
            heapq.heappush(self.big_min_heap, num)
        else:
            heapq.heappush(self.small_max_heap, -1*num)
        # After adding to heap, rebalance
        
        if len(self.small_max_heap) > len(self.big_min_heap):
            poped = -1 * heapq.heappop(self.small_max_heap)
            heapq.heappush(self.big_min_heap, poped)
        if len(self.small_max_heap) < len(self.big_min_heap):
            poped = heapq.heappop(self.big_min_heap)
            heapq.heappush(self.small_max_heap, -1 * poped)
        

    def findMedian(self) -> float:
        if len(self.small_max_heap) + len(self.big_min_heap) == 0:
            return 0
        if self.even:
            return ((-1 * self.small_max_heap[0]) +  self.big_min_heap[0])/2
        else:
            if len(self.small_max_heap) > len(self.big_min_heap):
                return -1 * self.small_max_heap[0]
            else:
                return self.big_min_heap[0]