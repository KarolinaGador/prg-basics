arr = [[0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0],
       [0,0,0,0,0]] 
op=1
for row in arr:
    for i in range(5):
       row[i]=(i+1)* op
    
       print(row[i], end='')
    op = op +1
       
    print()   

        