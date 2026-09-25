class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        list_to_recolor = set()

        def dfs(r,c, og_color, visited_set):
                # Return None always, change happens to the set.
                #If out of bounds, if not og_color, or if visited then skip.
            if min(r,c) < 0 or r == len(image) or c == len(image[0]) or image[r][c] != og_color or (r,c) in visited_set:
                return None
            visited_set.add((r,c))
            for next_ele in [(r-1, c), (r,c-1), (r+1,c), (r,c+1)]:
                dfs(next_ele[0], next_ele[1], og_color, visited_set)
        
        dfs(sr, sc, og_color = image[sr][sc], visited_set = list_to_recolor)

        for ele in list_to_recolor:
            image[ele[0]][ele[1]] = color
        
        return image