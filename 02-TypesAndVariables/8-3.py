###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

# celcious degrees
celsius = float(input('celsius degrees: '))
# celsius to kelvin
Kelvin = celsius + 273.15
# celsius to ferrenheit
farrenheit = (celsius*9/5) + 32
print(f'{celsius} celsius degrees is {Kelvin} kelvin degrees and {farrenheit} farrenheit degrees')