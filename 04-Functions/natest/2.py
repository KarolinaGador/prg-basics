def f(x, y):
    if x>0 and y>0:
        return '1 cwiartka'
    elif x<0 and y<0:
        return '3 cwiartka'
    elif y>0 and x<0:
        return '2 cwiartka'
    elif x>0 and y<0:
        return '4 cwiartka'
    
print(f(2, 4))    