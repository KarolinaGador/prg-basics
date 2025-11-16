dogs_humanage = int(input('Enter the dogs age in human years: '))

if dogs_humanage == 1:
  dogs_age = 10.5
  print(f'Dogs age in dogs years equals {dogs_age}')

elif dogs_humanage == 2:
  dogs_age = 21
  print(f'Dogs age in dogs years equals {dogs_age}')


elif dogs_humanage >= 2:
  dogs_age = 21 + (dogs_humanage-2)*4
  print(f'Dogs age in dogs years equals {dogs_age}')
else:
  print(f'Invalid age')