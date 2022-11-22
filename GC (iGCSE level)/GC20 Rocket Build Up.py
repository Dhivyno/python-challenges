time = 14

for i in range(0, 51):
  time += 1
  if time == 25:
    time = 1

if time > 12:
  print("the alarm should ring at", time - 12, "pm")
else:
  print("the alarm should ring at", time, "am")
