x = int(input('Enter x:'))
y = int(input('Enter y:'))

if x>0 and y>0:
    print(f'Point P({x},{y}) is in the first quadrant of the coordinate system')
elif y>0 and x<0:
    print(f'Point P({x},{y}) is in the second quadrant of the coordinate system')
elif y<0 and x<0:
    print(f'Point P({x},{y}) is in the third quadrant of the coordinate system')
elif y<0 and x>0:
    print(f'Point P({x},{y}) is in the fourth quadrant of the coordinate system')
else:
    print(f'Point P({x},{y}) is in the center of the coordinate system')