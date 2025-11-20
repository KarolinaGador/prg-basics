def month(n):
    if n==1:
        return 'january'
    elif n==2:
        return 'february'
    elif n==3:
        return 'march'
    elif n==4:
        return 'april'
    elif n==5:
        return 'may'
    elif n==6:
        return 'june'
    elif n==7:
        return 'july'
    elif n==8:
        return 'august'
    elif n==9:
        return 'september'
    elif n==10:
        return 'october'
    elif n==11:
        return 'november'
    elif n==12:
        return 'december'
    else:
        return "wrong number"
    
    
if __name__ == "__main__":
    print(month(4))
