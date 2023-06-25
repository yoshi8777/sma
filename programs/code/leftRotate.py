def leftrotate(m):
    n = len(m)
    rotated = [[] for _ in range(n)]

    for col in reversed(range(n)):
        for row in range(n):
            rotated[row].append(m[row][col])

    return rotated


matrix1 = [[1, 2], [3, 4]]
rotated1 = leftrotate(matrix1)
print(rotated1)  # Output: [[2, 4], [1, 3]]

matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotated2 = leftrotate(matrix2)
print(rotated2)  # Output: [[3, 6, 9], [2, 5, 8], [1, 4, 7]]


# def leftrotate(m):
#  n = len(m) # Get the size of the square matrix
#  # Step 1: Transpose the matrix
#  for i in range(n):
#  for j in range(i + 1, n):
#  m[i][j], m[j][i] = m[j][i], m[i][j]
#  # Step 2: Reverse each row
#  for i in range(n):
#  m[i] = m[i][::-1]
#  return m
# leftrotate([[1,2,3],[4,5,6],[7,8,9]])
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]