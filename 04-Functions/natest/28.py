def f(n):
    r1=0
    r2=0
    r5=0
    if n>=5:
      r5 = n//5
      aa = n%5
      if aa >=2:
         r2 = aa//2
         r1 = aa%2
      else:
         r1 = aa
    elif n>=2:
       r2 = n//2
       r1 = n%2
    elif n<2:
       r1=n
    return r1+r2+r5

print(f(8))      
               
         
