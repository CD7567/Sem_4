mat1 = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

mat2 = [[1, 4], 
        [2, 5], 
        [3, 6]]

if len(mat1[0]) == len(mat2):
    result = [[sum(a * b for a, b in zip(x_row, y_col)) for y_col in zip(*mat2)] for x_row in mat1]
else:
    result = "Incorrect input"

print(result)