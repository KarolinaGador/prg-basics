arr = [ 'Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy' ]
arr2 =[]
for i in arr:
    arr2.append(len(i))
a =max(arr2)
b=arr2.index(a)
print(arr[b])    


