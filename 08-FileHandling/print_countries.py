###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:

    for num, line in enumerate(file):
        print(num+1,line, end="")