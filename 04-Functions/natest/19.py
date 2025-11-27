def f(x, y):
    sum = 0
    for i in range (x, y+1):
        if int(i)%2==0 and int(i)%3==0 and int(i)%4!=0:
            sum = sum + int(i)
    return sum


print(f(10,30))