def f(pali):
    if pali[0:2]==pali[-1]+pali[-2]:
        return True
    else:
        return False
    
print(f('1221'))    