class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix_box_sum = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        
        self.matrix_box_sum[0][0] = matrix[0][0]
        
        for i in range(1, len(matrix)):
            self.matrix_box_sum[i][0] = self.matrix_box_sum[i-1][0] + matrix[i][0]
        for j in range(1, len(matrix[0])):
            self.matrix_box_sum[0][j] = self.matrix_box_sum[0][j-1] + matrix[0][j]

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                    self.matrix_box_sum[i][j] = self.matrix_box_sum[i - 1][j] + self.matrix_box_sum[i][j - 1] - self.matrix_box_sum[i - 1][j - 1] + matrix[i][j]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.matrix_box_sum[row2][col2]
        if row1 == 0:
            return self.matrix_box_sum[row2][col2] - self.matrix_box_sum[row2][col1-1]
        if col1 == 0:
            return self.matrix_box_sum[row2][col2] - self.matrix_box_sum[row1-1][col2]
        return self.matrix_box_sum[row2][col2] - self.matrix_box_sum[row2][col1-1] - self.matrix_box_sum[row1-1][col2] + self.matrix_box_sum[row1-1][col1-1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)