def f(dice):
 
 a = dice.count('1')   
 b = dice.count('2')  
 c = dice.count('3')  
 d = dice.count('4')  
 e = dice.count('5')  
 g = dice.count('6')  

 kk = max(a,b,c,d,e,g)

 if kk==a:
  return 1
 elif kk==b:
  return 2
 elif kk==c:
  return 3
 elif kk==d:
  return 4
 elif kk ==e:
  return 5
 elif kk==g:
  return 6
 
print(f('2133'))

