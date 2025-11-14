###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
def triangle_area(a,b,c):
    s = 1/2 * (a+b+c)
    result= float(math.sqrt(s(s - a)(s - b)(s - c) ))


    return result
values = triangle_area(int(input('Enter 1 number: ')), int(input('Enter 2 number: ')), int(input('Enter 3 number: ')))
print(f'The area of ​​a triangle with sides {} is {values}')
