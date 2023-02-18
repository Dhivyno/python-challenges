test = input("Is it raining? y/n ")
if test in ["y"]:
  print("Oh dear, no football today!")

#it prints it even if you say n because the print is not in the if statement 

test = input("Is it raining? y/n ")
if test in ["y"]:
  print("Oh dear, no football today!")
    
#if you type a capital Y, it does nothing becuase the print is only when you type in 'y' and not 'Y'

test = input("Is it raining? y/n ")
if test in ["y"]:
  print("Oh dear, no football today!")
    
#if they type in 'y' when the if statement is if it is 'Y' then nothing happens because the if statemnet is not satisfied 

test = input("Is it raining? y/n ")
if test in ["y", "yes"]:
  print("Oh dear, no football today!")
    
test = input("Is it raining? y/n ")
if test in ["Y"]:
  print("Oh dear, no football today!")
else:
print("great, we can play")
  
#there is no indent 