# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
food = 0
transport = 0
utilities =0
for row in monthly_expenses:
        food = food + row[0]
        transport= transport + row[1]
        utilities = utilities + row[2]
w1=0
w2=0
w3=0
w4=0
for a,roww in enumerate(monthly_expenses):
        for i in roww:
                if a==0:
                 w1 = w1 + i
                elif a ==1:
                 w2=w2 + i
                elif a ==2:
                 w3=w3 + i
                elif a ==3:
                 w4=w4 + i
total = 0
for rowww in monthly_expenses:
    for ii in roww:
      total = total + i


                
                


# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',w1)
print('Week 2:',w2)
print('Week 3:',w3)
print('Week 4:',w4)
print('---------------')
print('TOTAL:',total)