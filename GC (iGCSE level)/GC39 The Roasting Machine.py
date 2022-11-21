import random
list = [0, 1]
name = input("what is your name?  ")
insultsimulator = [("you look like something that", name, "drew with their left hand"), ("maybe you should eat some makeup so you can be as good looking as", name), ()] 
choice = random.choice(list)
print(*insultsimulator[choice])
#I CANT THINK OF ANY INSULTS 
