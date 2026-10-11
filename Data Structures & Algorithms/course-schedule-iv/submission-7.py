class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        top_sort = []
        visited = set()

        adj = {i : [] for i in range(numCourses)}

        for req in prerequisites:
            adj[req[1]].append(req[0])

        def dfs(node):
            if node in visited:
                return True
            visited.add(node)
            for child in adj[node]:
                dfs(child)
            top_sort.append(node)
        
        for ele in range(numCourses):
            dfs(ele)

        full_requirements = {}

        for ele in top_sort:
            full_requirements[ele] = set()
            for child in adj[ele]:
                full_requirements[ele].add(child)
                if child in full_requirements:
                    full_requirements[ele].update(full_requirements[child])
        to_return = []

        for query in queries:
            if query[0] in full_requirements[query[1]]:
                to_return.append(True)
            else:
                to_return.append(False)

        return to_return