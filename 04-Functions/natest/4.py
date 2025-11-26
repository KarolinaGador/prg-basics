def fib(n):
    a=0
    b=1
    
    if n==0:
     return 0
    if n==1:
     return 1
    
    for i in range(n-2):
     
     a, b=b, a+b
    return b


print(fib(9))