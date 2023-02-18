def Sort(a): 
  for i in range(1, len(a)): 
    key = a[i] 
    j = i-1
    while j >=0 and key < a[j] : 
      a[j+1] = a[j] 
      j -= 1
    a[j+1] = key 
  print("Sorted:") 
  for i in range(len(a)): 
    print(a[i]) 
  
  

a = [65, 72, 81, 7, 42, 9, 55, 89, 1] 
Sort(a) 
