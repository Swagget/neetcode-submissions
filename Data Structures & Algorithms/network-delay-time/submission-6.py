class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {i:[] for i in range(1, n+1)}
        for edge in times:
            adj[edge[0]].append([edge[2], edge[1]]) # Node -> (total_cost, destination)
        
        frontier_edges = []
        heapq.heapify(frontier_edges)
        heapq.heappush(frontier_edges, [0, k])

        reached = {}

        max_time_taken = 0

        while len(reached)<n and len(frontier_edges)>0: # This should work, else I can make it keys instead
            shortest_reach = heapq.heappop(frontier_edges)
            if shortest_reach[1] in reached: # If the node has been reached before, then skip
                continue
            max_time_taken = max(max_time_taken, shortest_reach[0])
            reached[shortest_reach[1]] = shortest_reach[0]

            for next_node in adj[shortest_reach[1]]:
                heapq.heappush(frontier_edges, [next_node[0] + shortest_reach[0], next_node[1]])
        
        if len(reached)<n:
            return -1
        
        return max_time_taken
