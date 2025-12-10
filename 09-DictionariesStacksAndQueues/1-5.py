countries = [
{"name":"Poland", "population":38000000},
 { "name":"Germany", "population":2310},
 { "name":"bPoland", "population":38000},
 { "name":"aPoland", "population":32300000},
 { "name":"ePoland", "population":2000},
]


for i in countries:
    for val in i.values():
        print(f'{val} ', end="" )
    print()    