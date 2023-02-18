m = int(input("Enter the number of rows:  "))
n = int(input("Enter the number of columns:  "))
array = []
buffer = []
highest = 0

for i in range(m):
  buffer = []
  for j in range(n):
    string = "Enter the element in row " + str(i+1) + " and column " + str(j+1) + ":  "
    element = int(input(string))
    buffer.append(element)
  array.append(buffer)

for i in range(m):
  for j in range(n):
    if array[i][j] > highest:
      rowindex = i+1
      columnindex = j+1
      highest = array[i][j]

print("The highest element was", highest, "located in row", rowindex, "and column", columnindex)