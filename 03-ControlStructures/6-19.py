q1 = input("Are you interested in computer science? (y/n): ") == "y"
q2 = input("Are you playing computer games? (y/n): ") == "y"
q3 = input("Do you have an Instagram account? (y/n): ") == "y"

if q1==True:
    ans1 = "yes"
else:
    ans1 = "no"
if q2==True:
    ans2 = "yes"
else:
    ans2 = "no"
if q3==True:
    ans3 = "yes"
else:
    ans3 = "no"      

print(f'Interested in computer science: {ans1}')
print(f'Playing computer games:{ans2}')
print(f'Has an Instagram account:{ans3}')