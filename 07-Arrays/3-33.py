arr =[[1,2,3,4,5],
     [1,2,3,4,5],
     [6,7,8,9,0]]
for row in arr:
    for i in row:
        pom = row[4]
        row[4] = row[0]
        row[0] = pom
        

print(arr)        