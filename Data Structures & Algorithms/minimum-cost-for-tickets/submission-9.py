class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        curr_costs = [0] * 366
        curr_costs[0] = 0
        days_set = set(days)
        for i in range(1, 366):
            if i in days_set:
                curr_costs[i] = min(curr_costs[i-1] + costs[0],
                                    curr_costs[max(0, i-7)] + costs[1],
                                    curr_costs[max(0, i-30)] + costs[2])
            else:
                curr_costs[i] = curr_costs[i-1]
        return curr_costs[-1]