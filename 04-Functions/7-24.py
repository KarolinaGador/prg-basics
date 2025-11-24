def f(expression) :
    total = 0
    current_op = 1   
    
    for ch in expression:
        if ch == '+':
            current_op = 1
        elif ch == '-':
            current_op = -1
        else:
            
            total += current_op * int(ch)
    
    return total
        


print(f('2+4'))
