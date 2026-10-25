class Node:
    def __init__(self, val): # Not sure what else I'd need
        self.parent = self
        self.val = val
        self.rank = 0

    def find_root(self): # finds the root of the nodes
        current = self
        while current.parent != current:
            current.parent = current.parent.parent
            current = current.parent
        return current

    @staticmethod
    def union(node_1, node_2): # union the nodes, if they are already connected, then return false
        root_1 = node_1.find_root()
        root_2 = node_2.find_root()
        if root_1 == root_2: # Ideally this should be checked before hand and we shouldn't have to come to this problem in general.
            return False
        if root_1.rank == root_2.rank:
            root_1.parent = root_2
            root_2.rank += 1
            return
        if root_1.rank < root_2.rank:
            root_1.parent = root_2
            return
        if root_1.rank > root_2.rank:
            root_2.parent = root_1
            return


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Create a helper function to find a minimum spanning tree, return the cost, and weight is -1 if it's disconnected. Also it should be able to force an edge, and also take the input of what edges we are considering.
        def MST(edges, forced_edge = None): # Forced edge can't be in the list of edges, make sure to remove it.
            nodes_dict = {}
            for node in range(n):
                nodes_dict[node] = Node(val = node)
            total_cost = 0
            total_edges = 0
            edges_used = []
            if forced_edge is not None: 
                Node.union(nodes_dict[forced_edge[0]], nodes_dict[forced_edge[1]])
                total_cost = forced_edge[2]
                total_edges = 1
                edges_used.append(forced_edge)

            sorted_edges = sorted(edges, key = lambda x:x[2])
            for edge in sorted_edges:
                if total_edges == n-1:
                    break
                if Node.union(nodes_dict[edge[0]], nodes_dict[edge[1]]) != False:
                    total_cost += edge[2]
                    total_edges += 1
                    edges_used.append(edge)
            if total_edges < n-1:
                return -1, edges_used
            return total_cost, edges_used

        init_cost, edges_used = MST(edges)

        critical_edges = []
        pseudo_critical_edges = []

        for edge_index, edge in enumerate(edges):
            if edge not in edges_used:
                continue
            temp_edges = edges.copy()
            temp_edges.remove(edge)
            current_cost, current_edges_used = MST(temp_edges)
            if current_cost != init_cost:
                critical_edges.append(edge_index)
        
        for edge_index, edge in enumerate(edges):
            if edge_index in critical_edges:
                continue
            temp_edges = edges.copy()
            temp_edges.remove(edge)
            current_cost, current_edges_used = MST(temp_edges, forced_edge = edge)
            if current_cost == init_cost:
                pseudo_critical_edges.append(edge_index)


        return [critical_edges, pseudo_critical_edges]