def f(arr):
    a = min(arr)
    b = max(arr)
    return b-a
def f2(arr):
    c = sorted(arr)
    d = len(arr) 
    if d%2!=0:
        return c[int((len(c)-1)/2)]
    if d%2==0:
        return (c[int(len(c))/2] + c[int(len(c)+2)/2])/2
    
def f3(arr):
    z = sorted(arr)
    n = len(arr)-1
    return z[-2]

def f4(arr):
    return max(arr), min(arr)

def f5(arr):
    res = ''
    for i in arr:
        if arr.index(i)!=len(arr) -1:
         res = res +str(i) + '-'
        else:
            res = res + str(i)
    return res 


print(f([7,3,8,5,2]), f2([7,3,8,5,2]), f3([7,3,8,5,2]),f4([7,3,8,5,2]), f5([7,3,8,5,2]))

    