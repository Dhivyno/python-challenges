def function(a,b):
  if a == 0:
    return b + 1
  elif a > 0 and b == 0:
    return function(a - 1,b + 1)
  else:
    return function(a - 1, function(a, b - 1))
print(function(3,3))
