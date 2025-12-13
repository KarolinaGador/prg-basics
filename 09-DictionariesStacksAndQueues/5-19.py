import json

with open('reservations.json','r', encoding='Utf-8') as file:
    hotel = json.load(file)


def num(plik):
 rooms=0
 for  value in hotel.values():
    for dict in value:
     rooms = len(dict)
    return rooms
 

 print(num(hotel))
       
        
