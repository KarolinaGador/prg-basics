def f(code):
    first = int(code[0])
    second = int(code[1])
    third = int(code[2])
    ilast = int(code[-1])

    if (first+second+third)%7==ilast:
        return True
    else:
        return False


print(f('7071'))    

