matrix = [['0', '1', '2', '3', '4', '5'],
 ['6', '7', '8', '9', '10', '11'],
['12', '13', '14', '15', '16', '17'],
['18', '19', '20', '21', '22', '23'],
['24', '25', '26', '27', '28', '29'],
['30', '31', '32', '33', '34', '35']]
          
length = len(matrix[0])

for i in range(length):
  buffer = ""
  for j in range(i+1):
    buffer += matrix[j][i-j] + " "
  print(buffer)

for i in range(length):
  buffer = ""
  for j in range(1, 6-i):
    buffer += matrix[j+i][6-j] + " "
  print(buffer)
