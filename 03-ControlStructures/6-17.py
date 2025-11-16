time_24 = input('Enter time (24-hour format): ')
hours_24 = int(time_24[0:2])
minutes = int(time_24[3:5])

if hours_24 <12:

    print(f'Time in 12-hour format: {time_24}am')
elif hours_24 == 12 and minutes>=1:
    time_12=time_24
    print(f'Time in 12-hour format: {time_12}pm')
elif hours_24==12 and minutes==0:
    print(f'Time in 12-hour format: 12:00')
elif hours_24>12:
    hours_12= hours_24-12
    print(f'Time in 12-hour format: {hours_12}:{minutes}pm')