def f(pas):
 a = len(pas)   
 if a<6:
  return False
 
 for i in pas:
  b = pas.count(i)
  if b>1:
   return False
 return True
 

print(f(''))
        
        
