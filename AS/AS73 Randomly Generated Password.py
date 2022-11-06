import random
chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "<", ">", "?", ":", ":", ",", ".", "/", ";", "{", "}", "[", "]", "-", "=", "|"]

masterlist = []
password = ""

color = list(input("Enter your favorite color:  "))
place = list(input("Enter your favorite place:  "))
animal = list(input("Enter your favorite animal:  "))

for i in range(len(color)):
  masterlist.append(color[i])
for i in range(len(place)):
  masterlist.append(place[i])
for i in range(len(animal)):
  masterlist.append(animal[i])

for i in range(10):
  password += random.choice(masterlist)

for i in range(6):
  password += random.choice(chars)

print(password, "is your randomly generated password!")
