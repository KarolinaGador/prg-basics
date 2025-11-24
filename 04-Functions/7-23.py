def f(password):

   for i in password:
      charcount = password.count(i)
      if len(password)<6:
         return False
      elif charcount>1:
         return False
      elif len(password)>=6 and charcount==1:
         return True
   return False


print(f(''))
      

      