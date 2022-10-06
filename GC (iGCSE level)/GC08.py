weight = float(input("Enter your weight in kilograms:  "))
height = float(input("Enter your height in meters:  "))
a = weight/(height**2)

if a < 18.5:
  print("Underweight")
elif 18.5<=a<25:
  print("Normal weight")
elif 25<=a<30:
  print("Overweight")
elif a >=30:
  print("Obese")
