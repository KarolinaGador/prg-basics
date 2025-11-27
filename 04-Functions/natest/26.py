def f(x,y):
    counter = 0
    for i in range(x,y+1):
        if i<0 and i%2==0:
          counter = counter +1
    return counter      

print(f(-1,11))          