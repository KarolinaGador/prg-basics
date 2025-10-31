###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = float(input('a='))
b = float(input("b="))
c = float(input("c="))
cuboid_volume = a*b*c
cuboid_surface = 2*a*b + 2*b*c + 2*c*a
print(f'the volume of cuboid is {cuboid_volume} and the surface is {cuboid_surface}')