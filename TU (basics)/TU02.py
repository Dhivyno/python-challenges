a = input("What is your name?")
print("Hello", a)

einstein_age = 1879
my_age = input("When were you born?  ")
difference = int(my_age) - int(einstein_age)
if int(my_age) < int(einstein_age):
    print("How are you even alive right now?")
else:
    print("Einstein is", difference, "years older than you")

name_celeb = input("What is your celebrity's name?  ")
age_celeb = int(input("When was your celebrity born (year)? "))
my_age = int(input("When were you born?  "))
difference = int(my_age) - int(age_celeb) 
print(name_celeb , "is", difference, "years older than you")
