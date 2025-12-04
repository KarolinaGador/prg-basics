arr1 = [7,9,2,4,5,6]
arr2 = [2,4,6,1]

for i in arr2:
    if i not in arr1:
        result = False
    else:
        result = True

print(result)        

