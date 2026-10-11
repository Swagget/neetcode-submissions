class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i:[] for i in range(numCourses)}
        for req in prerequisites:
            adj[req[0]].append(req[1])

        to_return = []
        visited = set()
        current_path = []
        
        def dfs(node):
            if node in current_path:
                return False

            if node in visited:
                return True
            visited.add(node)
            current_path.append(node)

            for child in adj[node]:
                if not dfs(child):
                    return False
            to_return.append(node)
            
            current_path.pop()
            return True

        for node in range(numCourses):
            if not dfs(node):
                return[]

        
        if len(to_return)<numCourses:
            return []
            
        return to_return