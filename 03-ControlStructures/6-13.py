car_speed = int(input('Enter your car speed: '))
speed_limit_min = 40
speed_limit_max = 140

if car_speed <40 or car_speed>140:
    print(f'Your car speed is: {car_speed} Warning! invalid car speed')
elif car_speed>=40 and car_speed<=140  :
  print(f'Your car speed is: {car_speed}')  
else:
   print('invalid data')