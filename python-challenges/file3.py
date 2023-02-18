with open("counter2.txt","r") as whole_file:
  for line in whole_file:
    b = line
    print(str(line)+"\n")

with open("counter2.txt","a") as existing_file:
    for i in range(int(b)+1,int(b)+11):
        line_to_write = "\n"+str(i)
        existing_file.write(line_to_write)