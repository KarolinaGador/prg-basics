def f(n): 
 if n ==1:
  return '*'
 elif n>0:
  first = '*'
  last = '*'
  return '*/' * (n-1) + last
 elif n == 0:
  return " "
 else:
  return "wrong data"
  
    

 


print(f(4))