def setZeroes(matrix):
  m,n=len(matrix),len(matrix[0])
  row=[0]*m
  col=[0]*n
  for i in range(len(matrix)):
    for j in range (len(matrix[i])):
      if matrix[i][j] == 0:
        row[i]=1
        col[j]=1
  for i in range (len(row)):
    for j in range (len(col)):
      if row[i] == 1 or col[j] ==1:
        matrix[i][j]=0
  