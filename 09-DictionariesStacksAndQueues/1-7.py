comp = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

for key, val in comp.items():
    print(key, val)
total = 0
for val in comp.values():
 total = total + int(val)

print(total)