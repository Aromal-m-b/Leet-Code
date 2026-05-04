class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        new = []
        row = []
        for i in range (0,len(matrix)):
            for j in range (len(matrix)-1,-1,-1):
                row.append(matrix[j][i])
            new.append(row)
            row = []
        matrix[:] = new