from functools import reduce
numbers = [2,4,6,3,7,5]

evenn = filter(lambda x: x%2==0, numbers)
total_sum = reduce(lambda x, y: x + y, evenn)
print(total_sum)