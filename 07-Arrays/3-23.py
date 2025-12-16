def f(tekst):
 b = tekst.split()
 a=len(b)
 return a 

def f3(tekst):
  b = tekst.split()
  c=[]
  for i in sorted(b):
    c.append(i)
  return c  

def f2(tekst):
  b = tekst.split()
  c=[]
  for i in sorted(b, key=len):
    c.append(i)
  return c  



 



print(f2('An apple a day keeps the doctor away'))