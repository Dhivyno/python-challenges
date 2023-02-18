matrix = [[1, 3, 7, 9, 16], [6, 2, 4, 1, 8], [8, 9, 10, 12, 14], [7, 5, 1, 4, 11]]
num = 0
def check(D, H, i, j):
  global num
  try:
    if abs(H[i+1][j] - H[i][j]) < D:
      num += 1
      check(D, H, i+1, j)
  except:
    pass
  try:
    if abs(H[i][j+1] - H[i][j]) < D:
      num += 1
      check(D, H, i, j+1)
  except:
    pass
  print(num)

check(5, matrix, 1, 1)

    
      