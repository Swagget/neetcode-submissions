class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        to_return = [[0] * len(matrix) for ele in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                to_return[j][i] = matrix[i][j]
        
        return to_return