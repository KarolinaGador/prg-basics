import json

szymon = {
'wiek':19,
'studia' :'chemia',
'uczelnia' : 'WAT',
'Czy_go_kocham' : True,
'wzrost' : 180,
}

with open('favourite.json','w') as file:
    json.dump(szymon, file, indent=4)