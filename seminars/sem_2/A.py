mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

transponed = [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
print(transponed)