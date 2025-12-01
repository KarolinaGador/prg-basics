arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[len(arr)-2])
print('sum of first and last', arr[0] + arr[-1])
print('middle value', arr[int((len(arr)-1)/2)])
for i in arr:
    print(str(i) + ' ', end='')
