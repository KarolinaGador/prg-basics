number = int(input("Enter your number: "))
if number >0:
  sign = "positive"
elif number <0:
  sign = "negative"  
else:
  sign="0"  
print(f'number {number} is {sign}')