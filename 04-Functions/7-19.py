def f(number):
 snumber = str(number)
 res = 0
 for i in snumber:
  a = snumber.count(i)
  if a> 1:
   res = res + int(i)
 return res   

print(f(513553007))
