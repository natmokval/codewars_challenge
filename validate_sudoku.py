# https://www.codewars.com/kata/540afbe2dc9f615d5e000425/python
# Validate Sudoku with size `NxN`

import math
class Sudoku(object):
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        arr = self.data
        rows = len(arr)
        cols = [len(arr[:][i]) for i in range(0, rows)]
        little_square = int(math.sqrt(rows))
        if len(set(cols)) > 1 or rows != cols[0] or math.sqrt(rows) != little_square or isinstance(arr[0][0], bool):
            return False
        
        arr_tr = [[arr[i][j] for i in range(0, rows)] for j in range(0, rows)]
        res_r = [set(arr[j]) == set(range(1, rows+1)) for j in range(0, rows)]
        res_c = [set(arr_tr[j]) == set(range(1, rows+1)) for j in range(0, rows)]
        return all(res_r) and all(res_c) and self.is_valid_little_squares(arr, rows, little_square) and True
    
    def is_valid_little_squares(self, arr, rows, little_square):
        grids = [
            [arr[m][n] for n in range(j, j + little_square) for m in range(i, i + little_square)]
            for j in range(0, rows, little_square)
            for i in range(0, rows, little_square)
        ]
        return all([len(set(grids[i])) == rows for i in range(0, rows)])
    