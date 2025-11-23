def f(number, even):
    anumber = abs(number)
    asnumber = str(anumber)
    i = 0
    for char in asnumber:
        licz = int(char)
        if even == True:
         if licz%2==0:
          i = i + licz
          
        elif even == False:
         if licz%2!=0:
          i = i + licz
          
    return i



print(f(23231, True))       

