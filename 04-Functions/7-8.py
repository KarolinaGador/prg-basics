def f(amount):
    result5 =0
    result2= 0
    result3 =0  
    if amount >=5:
        result5 = amount//5
        rim = amount%5
        if rim>=2:
            result2 = rim//2
            result3 = rim%2
        else:
            result3 = rim    

    elif amount >= 2 and amount <5:
       result2 = amount//2
       result3 = amount%2

    elif amount <2:
       result3 = amount

    return result5 + result2 + result3
    
    
if __name__ == "__main__": 
   print(f(23))