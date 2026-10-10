class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = {i:[] for i in range(n)} # Node -> [[prob, dest_node], [prob, dest_node]...]

        for index, edge in enumerate(edges):
            adj[edge[0]].append([succProb[index], edge[1]]) 
            adj[edge[1]].append([succProb[index], edge[0]]) 
        
        reached = {}

        unchecked = [[-1, start_node]] # Sorted by the first index, which is the probability of reaching that node.
        heapq.heapify(unchecked)

        while len(unchecked) > 0:
            next_node = heapq.heappop(unchecked)
            if next_node[1] in reached:
                continue
            reached[next_node[1]] = next_node[0] * -1

            for new_possibility in adj[next_node[1]]:
                if new_possibility[1] in reached:
                    continue
                heapq.heappush(unchecked, [new_possibility[0] * next_node[0], new_possibility[1]]) # to the frontier we push the [next_prob, next_node]
            
            if end_node in reached:
                return reached[end_node]
        return 0