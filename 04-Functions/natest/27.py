def f(number,even):
    snumber = str(number)
    sum = 0
    if even==True:
        for i in snumber:
            if int(i)%2==0:
                sum = sum + int(i)
    elif even == False:
        for i in snumber:
            if int(i)%2!=0:
                sum = sum + int(i)

    return sum

print(f(3124, True))                            

