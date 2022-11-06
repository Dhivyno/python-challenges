import random
phrases = ["It is certain", "Without a doubt", "Ask again later", "You may rely on it", "It is decidely so", "Very doubtful", "Don't count on it"]

question = input("What is your yes or no question?  ")
pick = random.choice(phrases)
print(pick)
