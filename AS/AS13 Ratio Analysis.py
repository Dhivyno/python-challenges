gross = int(input("What is your gross profit?  "))
net = int(input("What is your net profit?  "))
sales = int(input("How many sales did you make?  "))

gpm = gross/sales*100
npm = net/sales*100

print("Your GPM is", gpm, "%")
print("Your npm is", npm, "%")
