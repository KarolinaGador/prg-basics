def f(number):
    snumber = str(number)
    a=0
    sum =0
    for i in snumber:
     a = snumber.count(i)
     if a>1:
        sum = sum + int(i)
    return sum

print(f(1027))    

