#EX 1: The IF statement doesn’t work if it is not indented
#It will end the code as there is nothing that says to do anything if it is a capital “Y”
#If the user enters “Y” it will work perfectly but if they enter “y” then it will end the program

test = input("Is it raining? y/n ")
list = ["y", "Y", "yes", "Yes"]
if test in list:
    print("Oh dear, no football today!")

test = input("Is it raining? y/n ")
list = ["y", "Y", "yes", "Yes"]
if test in list:
    print("Oh dear, no football today!")
else:
    print("Yay!, we can play football today!")
