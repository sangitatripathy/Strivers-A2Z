def transpose(matrix):
  matrix=list(map(list,zip(*matrix)))
  return matrix
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(transpose(matrix))