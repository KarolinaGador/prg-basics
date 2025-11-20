def hide(number):
    innumber = str(number)
    result = ""
    counter = 0

    for i in innumber:
        counter += 1

        # pierwsze 2 cyfry
        if counter <= 2:
            result += i
        # środkowe (od 3 do 12)
        elif counter > 3 and counter < 13:
            result += "*"
        # ostatnie 4 cyfry (od 13 w górę)
        elif counter > 12:
            result += i

    return result


if __name__ == "__main__": 
    print(hide(5290312400019022))
   

    
