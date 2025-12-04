arr = [7,9,2,4,5,6]
even =[]
odd=[]
for i in arr:
    if int(i)%2==0:
        even.append(i)
    elif int(i)%2!=0:
        odd.append(i)
aarr = even + odd 

print(aarr)         
