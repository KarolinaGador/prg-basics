matrix = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# Replace the main diagonal with 1
for i in range(len(matrix)):
    matrix[i][i] = 1

# Print the modified matrix
for row in matrix:
    print(*row)