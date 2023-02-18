with open("rudyard.txt","r") as whole_file:
  for line in whole_file:
    prompt = input("type yes to move onto the next line or end to end the program.   ")
    if prompt in ["y", "Y", "yes", "YES", "Yes"]:
      print("\n\n ", line,end="")
    elif prompt == "end":
      break

