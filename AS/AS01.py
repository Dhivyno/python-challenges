def bubbleSort(a): 
  n = len(a) 
  for i in range(n-1): 
    for j in range(0, n-i-1): 
      if a[j] > a[j+1] : 
        a[j], a[j+1] = a[j+1], a[j] 
  

a = [89,12,9,88,91,3,55,31] 
  
bubbleSort(a) 
  
print ("Sorted array is:") 
for i in range(len(a)): 
  print (a[i])  
