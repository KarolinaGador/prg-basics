arr = [[-38, 19], [5, 40], [-7, 11], [29, 16]]

min_val = min(min(row) for row in arr)
max_val = max(max(row) for row in arr)

# znajdź pozycje
for r in range(len(arr)):
    for c in range(len(arr[r])):
        if arr[r][c] == min_val:
            min_pos = (r, c)
        if arr[r][c] == max_val:
            max_pos = (r, c)

print("Smallest:", min_val, "at", min_pos)
print("Largest:", max_val, "at", max_pos)