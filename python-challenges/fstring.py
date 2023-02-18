var = float(input("How many ringgits do you have?  "))

print(f"RM{var}")

num1 = [1,1003442,5.32222342]
num2 = [5.62233,7.364363,9.32747474342]
num3 = [9.2634526,7.866832817,10.781237892798]

print("\nlowest to highest\tlowest to highest\tlowest to highest\nfirst list\t\t\tsecond list\t\t\tthird list")
for i in range(len(num1)):
    print(f"{num1[i]:^15} {num2[i]:^17} {num3[i]:^23}")

number = int(input("What is your number that you want to covert to binary?  "))
