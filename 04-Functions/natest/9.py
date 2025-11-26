def f(number, even):
    sum=0
    inumber = str(number)
    if even==True:
        for i in inumber:
            if int(i)%2==0:
             sum = sum + int(i)
    

    elif even==False:
       for i in inumber:
          if int(i)%2!=0:
             sum = sum + int(i)

    return sum


print(f(22312, False))
                