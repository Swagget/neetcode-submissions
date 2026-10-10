class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = {i:[] for i in range(len(points))}

        for i in range(len(points)):
            for j in range(i, len(points)):
                dist_i_j = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                adj[i].append([dist_i_j, j])# each element in the adjacency list is [dist, j].
                adj[j].append([dist_i_j, i])# each element in the adjacency list is [dist, j].
        
        available_edges = [ele.copy() for ele in adj[0]]
        visited = set([0])

        heapq.heapify(available_edges)

        total_cost = 0

        while len(visited)<len(points):
            cheapest_edge = heapq.heappop(available_edges)
            if cheapest_edge[1] in visited:
                continue
            else:
                total_cost += cheapest_edge[0]
                visited.add(cheapest_edge[1])
                for next_edge in adj[cheapest_edge[1]]:
                    heapq.heappush(available_edges, next_edge)

        return total_cost