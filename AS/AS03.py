a = [0]
text = input("Enter text:  ")
for i in range(len(text)-1, -1, -1):
  a.append(text[i])

print(*a[1::], sep = "")
