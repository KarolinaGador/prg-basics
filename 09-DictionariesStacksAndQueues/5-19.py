import json

with open('reservations.json','r', encoding='Utf-8') as file:
    hotel = json.load(file)


def num(plik):
 rooms=0
 for  value in hotel.values():
    for dicta in value:
     rooms = rooms + 1
 return rooms

def paid(plik):
  counter =0
  for  value in hotel.values():
    for dicta in value:
      if dicta['paid']==True:
          counter = counter + 1
      else:
          continue  
    return counter  

def unpaid(plik):
   counter =0
   for  value in hotel.values():
    for dicta in value:
      if dicta['paid']==False:
          counter = counter + 1
      else:
          continue  
    return counter 

def vpaid(plik):
   values = 0
   for  value in hotel.values():
    for dicta in value:
      if dicta['paid']==True:
         values = values + int(dicta["price_per_night"])*int(dicta['nights'])   
    return values

def npaid(plik):
   values = 0
   for  value in hotel.values():
    for dicta in value:
      if dicta['paid']==False:
         values = values + int(dicta["price_per_night"])*int(dicta['nights'])   
    return values         
   
         

              

 

print(num(hotel))
print(paid(hotel))
print(unpaid(hotel))
print(vpaid(hotel))
print(npaid(hotel))
       
        
