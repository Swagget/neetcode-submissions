class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        edge_to_remove = None
        for edge in edges:
            if edge[0] not in parent:
                parent[edge[0]] = edge[0]
            if edge[1] not in parent:
                parent[edge[1]] = edge[1]

        def true_parent(node):
            while parent[node] != node:
                node = parent[node]
            return node
                
        for edge in edges:
            if true_parent(edge[0]) == true_parent(edge[1]):
                edge_to_remove = edge
            min_root = min(true_parent(edge[0]), true_parent(edge[1]))
            max_root = max(true_parent(edge[0]), true_parent(edge[1]))
            parent[edge[0]] = min_root
            parent[edge[1]] = min_root
            parent[max_root] = true_parent(min_root)
        return edge_to_remove