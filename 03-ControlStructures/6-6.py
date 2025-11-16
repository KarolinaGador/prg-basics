hours = int(input('Enter how many hours of parking: '))

if hours == 1 or hours == 2:
    print('Parking costs 5 PLN')
elif hours >=3 and hours <=6:
    print('Parking costs 15 PLN')   
elif hours > 6:
    print('Parking costs 20 PLN')