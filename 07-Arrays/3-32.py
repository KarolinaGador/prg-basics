arr =[[1,2,3,4,5],
     [1,2,3,4,5],
     [6,7,8,9,0]]




pom = arr[2]
arr[2]=arr[0]
arr[0]=pom
print(arr, end='')
   