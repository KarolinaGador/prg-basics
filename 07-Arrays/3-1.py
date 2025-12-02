arr = [34,7,19,4,21,8]
counter = 0
evencounter = 0
while counter<len(arr):
    if arr[counter]%2==0:
        evencounter = evencounter + 1
    counter = counter + 1       

print(evencounter)        

