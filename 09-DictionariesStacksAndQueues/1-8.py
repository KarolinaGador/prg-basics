price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

for key, val in price_list.items():
    print(key, val)

total1=0
for val in price_list.values():
 total1 = total1 +int(val)
print(total1)
total2=0
for keyy, vall in price_list.items():
   new = float(vall)*0.9
   price_list[keyy] = new
   total2=total2 + new
   print(f'{keyy} {new:.2f}')

print(total2)   