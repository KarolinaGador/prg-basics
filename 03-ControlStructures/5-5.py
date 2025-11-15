###
# Sums numbers entered by user
#
total_sum = 0
aritmetic_mean = 0


while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count += 1
     
if count > 0:
    aritmetic_mean = total_sum / count
else:
    aritmetic_mean = 0
    
print(f"The total sum of the numbers is: {total_sum} the aritmetic mean is {aritmetic_mean}")