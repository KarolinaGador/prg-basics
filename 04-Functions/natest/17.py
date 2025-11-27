def f(code):
    sum = int(code[0]) + int(code[1]) + int(code[2])
    lastdigit = sum%7

    if code[3]==str(lastdigit):
        return True
    else: 
        return False
    

print(f('1114'))    


