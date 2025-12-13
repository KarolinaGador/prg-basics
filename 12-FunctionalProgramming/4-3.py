arr = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
bez2 = list(filter(lambda x: x>2.0, arr))
mean = list(map(lambda x: sum(x)/len(arr),bez2))
print(mean)