class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.preSum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix[r][c]
                # r+1 is r in original matrix
                above = self.preSum[r][c+1]
                self.preSum[r+1][c+1] = above + prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2 = row1+1,col1+1,row2+1,col2+1
        btmRight = self.preSum[row2][col2]
        abv = self.preSum[row1-1][col2]
        left = self.preSum[row2][col1-1]
        topLeft = self.preSum[row1-1][col1-1]
        res = btmRight - (abv+left) + topLeft
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)