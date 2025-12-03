arr=[2, 3, 2, 5, 8, 1, 9, 8]
res=""
for i in arr:
    if arr.count(i)==1:
        res = res + str(i)

print(res)        
