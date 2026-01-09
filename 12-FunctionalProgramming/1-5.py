def f(distance, hours, minutes):
    min = minutes/60
    return distance/(hours + min)

print(f(70,1,23))