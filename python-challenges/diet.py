def main1():
  number = int(input("how many different foods did you eat today?  "))
  a = input("What is the name of your first food?  ")
  if isinstance(a, int):
    return
  cal1 = input("How many calories did you consume?  ")
  if type(cal1) == "str":
    return

  listname = [a]
  listcal = [cal1]
  for i in range(number - 1):
    b = input("what is the name of the next food that you ate?  ")
    cal2 = int(input("how many calories did you consume with this food?  "))
    listname.append(b)
    listcal.append(cal2)

main1()