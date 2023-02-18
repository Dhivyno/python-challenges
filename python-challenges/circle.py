from math import pi

r = float(input("What is the radius of your circle?  "))

cir = 2 * pi * r
print("The circumference of circle is", round(cir, 2))
area = pi * r**2
print("The area of circle is", round(area, 2))