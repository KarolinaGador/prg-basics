hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]


def hl(hotels):
    li= []
    for hotel in hotels:
     li.append(hotel['name'])
    return ", ".join(li)
    
print(hl(hotels_in_Krakow))    

def ap(hotels):
   price1 = 0
   counter =0
   for price in hotels:
      price1 = int(price1) + int(price["price"])
      counter = counter + 1
   avg = price1/counter
   return avg
print(ap(hotels_in_Krakow))   


