def f(exp):
    res = 0
    op =1
    for i in exp:
        if i=='+':
            op = 1
        elif i =="-":
            op=-1
        else:    
         res = res + op *int(i)
    return res


print(f('2-1+3+1'))

        
