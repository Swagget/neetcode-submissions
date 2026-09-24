import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_stones = [-ele for ele in stones]
        heapq.heapify(negative_stones)
        while len(negative_stones) > 1:
            largest = heapq.heappop(negative_stones)
            second_largest = heapq.heappop(negative_stones)
            if largest == second_largest:
                continue
            else:
                new_weight = largest - second_largest
                heapq.heappush(negative_stones, new_weight)
        if len(negative_stones) == 1:
            return -1 * negative_stones[0]
        else:
            return 0