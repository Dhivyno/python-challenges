import math
massnum = float(input("What is the mass of the planet?  "))
radiusnum = float(input("What is the radius of the planet?  "))
g = 6.6743*(10**-11)

class Planet():
   def __init__(self, mass, radius, escape):
      self.mass = mass
      self.radius = radius
      self.escape = escape

Planet.escape = math.sqrt(2*g*massnum/radiusnum)

print(Planet.escape)

