def f(sentence):
 s = ""
 for i in sentence:
  if i != " ":
   s = s + i   
 return s  


print(f('integrated development environment'))