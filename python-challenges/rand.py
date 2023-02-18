import random
mynumber = random.uniform(0.1, 9.9)
print(round(mynumber,1))

Choose_Name = ["James","John","Mark","Rick"]
for i in range(1,5):
    chosen = random.choice(Choose_Name)
    print(chosen)
    choice = input("Do you want to keep this name in the list?  ")
    if choice in ["y", "Y", "yes", "Yes"]:
      print(Choose_Name)
    else:
      Choose_Name.remove(chosen)
      print(Choose_Name)