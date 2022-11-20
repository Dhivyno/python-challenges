a = [1, 1]
for i in range(98):
    next_num = a[i] + a[i + 1]
    a.append(next_num)

print(a)
print(len(a))
