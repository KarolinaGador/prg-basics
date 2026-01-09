dict = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

cities = list(filter(lambda x: dict[x]>0, dict))
print(cities)