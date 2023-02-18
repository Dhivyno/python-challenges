lights = []
counter = 0
for i in range(1000):
  lights.append(".")

with open("lightsinput.txt", "r") as file:
  for line in file:
    for i in range(len(line)):
      if line[i] == " ":
        start = int(line[0:i])
        end = int(line[i+1:])
    if start > end:
      buffer = end
      end = start
      start = buffer
    for i in range(start, end+1):
      if lights[i] == ".":
         lights[i] = "X"
      elif lights[i] == "X":
        lights[i] = "."
print(lights)
for i in range(len(lights)):
  if lights[i] == "X":
    counter += 1
print(counter)