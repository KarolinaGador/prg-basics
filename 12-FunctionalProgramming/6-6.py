arr = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]
jest = list(map(lambda e: e[0].upper()+", "+ e[1], arr))
print(jest)