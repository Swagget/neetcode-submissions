class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        roots = [i for i in range(n)]
        ranks = [0] * n
        
        def find_root(index):
            if roots[index] != index:
                roots[index] = find_root(roots[index])
            return roots[index]
        
        def join(index_1, index_2):
            root_1 = find_root(index_1)
            root_2 = find_root(index_2)
            if root_1 == root_2:
                return
            rank_1 = ranks[root_1]
            rank_2 = ranks[root_2]
            if rank_1 < rank_2:
                roots[root_1] = root_2
            elif rank_1 > rank_2:
                roots[root_2] = root_1
            else:
                roots[root_1] = root_2
                ranks[root_2] += 1

        for edge in edges:
            join(edge[0], edge[1])

        return len({find_root(i) for i in range(n)})