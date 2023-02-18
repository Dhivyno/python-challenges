def search(a, x): 
  for i in range(len(a)): 
    if a[i] == x: 
      print(i,"th place", sep = "")
  

a = [10, 20, 45, 51, 23, 73, 81, 9, 34]
search(a, 73)