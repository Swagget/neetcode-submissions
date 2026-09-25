class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        side_length = len(grid)
        if grid [0][0] == 1 or grid [side_length-1][side_length-1] == 1:
            return -1
        length = 1
        queue = deque()
        visited = set()
        queue.append((0,0))
        visited.add((0,0))
        movements = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        while len(queue) > 0:
            current_level_length = len(queue)
            for _ in range(current_level_length):
                current_position = queue.popleft()
                visited.add(current_position)
                if current_position == (side_length-1,side_length-1):
                    return length
                
                for move in movements:
                    next_position = (current_position[0] + move[0], current_position[1] + move[1])
                    if next_position[0] < 0 or next_position[1] < 0 or next_position[0] == side_length or next_position[1] == side_length or grid[next_position[0]][next_position[1]] == 1 or next_position in visited:
                        continue
                    queue.append(next_position)
                    visited.add(next_position)
            length += 1
        return -1