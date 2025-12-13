import json
with open('dogs.json','r',encoding='utf-8') as file:
    psy = json.load(file)

for dogs in psy:
    for key, value in dogs.items():
     if dogs['age']<5:
        print(key,':',value)
     else:
        continue   
