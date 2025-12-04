arr = [7,3,8,5,2]
number = input('Enter your number: ')
res = ''
for i in arr:
    if int(i)>int(number):
        res = res + str(i) + ' '
print(res)    
