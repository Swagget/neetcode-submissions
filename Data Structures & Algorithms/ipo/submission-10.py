class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        current_capital = w
        max_available_project = [] # This is the list of valuations, in a heap. And this is linked directly to profits to projects. And some valuations might be here multiple times. Because profits to proejects is an int to a list.
        heapq.heapify(max_available_project)
        capital_heap = []
        heapq.heapify(capital_heap)
        capital_to_profits = {}

        total_profit = 0

        for capital, profit in zip(capital, profits):
            capital_to_profits[capital] = capital_to_profits.get(capital, []) + [profit]
        for capital in capital_to_profits.keys():
            heapq.heappush(capital_heap, capital)

        for project_taken in range(k):
            if len(capital_heap) > 0:
                while capital_heap[0] <= current_capital:
                    next_cheapest_capital_available = heapq.heappop(capital_heap)
                    for ele in capital_to_profits[next_cheapest_capital_available]:
                        heapq.heappush(max_available_project, -1 * ele)
                    if len(capital_heap) == 0:
                        break
            if len(max_available_project) == 0:
                break
            total_profit += -1 * heapq.heappop(max_available_project)
            current_capital = total_profit + w

        return total_profit + w