def f(number):
    snumber = str(number)
    a=0
    s=0
    for i in snumber:
     a=  snumber.count(i)
     if a>1:
      s = s + int(i)

    return s


print(f(513553007))
       
