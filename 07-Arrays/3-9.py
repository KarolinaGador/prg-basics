def f(ar1, ar2):
    
    if len(ar1)!=len(ar2):
        return False
    for i in range(len(ar1)):
            if ar1[i] != ar2[i]:
             return False
            
    else:
       return True

print(f( [5,3,1],   [5,3,1]))    

        
