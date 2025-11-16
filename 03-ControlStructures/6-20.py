decimal = int(input('Enter decimal number: '))
reminder = []
aa = decimal
while decimal>0:
  remain = decimal%2 
  decimal = decimal//2
  reminder.append(remain)

reminder.reverse()
binary = ""
for bit in reminder:
    binary = binary + str(bit)
 
print(f'decimal {aa} binary {binary} ') 