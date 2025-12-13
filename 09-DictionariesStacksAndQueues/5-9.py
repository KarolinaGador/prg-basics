
wojewodztwa ={}
with open('province.csv','r', encoding='utf-8') as prowi:
  
  for line in prowi:
   lines = line.strip().split(',')
   if lines[0] =='Letter' and lines[1]=='Name':
    continue
   wojewodztwa[lines[0]] = lines[1]
wynik = {}
with open('vehicle.txt', 'r', encoding='utf-8') as cars:
  auta = cars.read().splitlines()
  for key, val in wojewodztwa.items(): 
    counter = 0
    for car in auta:
     if car[0] == key:
      counter = counter + 1
    wynik[val] = counter

print(wynik)



 
    
 

   