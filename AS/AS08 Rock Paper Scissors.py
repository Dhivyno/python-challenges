import random
pick = input("Pick rock, paper or scissors:  ")
choices = ["rock", "paper", "scissors"]

comp = random.choice(choices)
if comp == pick:
  print("It's a tie! The computer picked", pick, "as well")
if (comp == "rock" and pick == "paper") or (comp == "paper" and pick == "scissors") or (comp == "scissors" and pick == "rock"):
  print("You won! The computer picked", comp)
if (pick == "rock" and comp == "paper") or (pick == "paper" and comp == "scissors") or (pick == "scissors" and comp == "rock"):
  print("You lose! The computer picked", comp)
