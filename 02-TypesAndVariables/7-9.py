import random
dice_rolled = random.randint(1,6)
special = dice_rolled == 1 or dice_rolled == 6
print(f'your number {dice_rolled} special number {special}')
