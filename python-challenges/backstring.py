a = []
v = str(input("Enter string:  "))
for i in range(len(v)-1, -1, -1):
  a.append(v[i])
print(*a, sep = "")