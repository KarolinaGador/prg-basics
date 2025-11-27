def f(expr):
    result = 0
    op = 1
    for i in expr:
        if i=='+':
            op=1
        elif i =='-':
            op = -1
        else:
            result = result + op*int(i)
    return result


print(f('3-4+6-9'))



