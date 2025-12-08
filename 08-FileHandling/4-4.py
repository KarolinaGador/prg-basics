import re
plik=open('it_company.csv','r')
dane=[]
for linia in plik:
    dane.append(linia)
k=1
for i in range(5):
    print(dane[k])
    
    k+=1

while re.match(input("press enter key"),""):
    for i in range(5):
        print(dane[k])
        k+=1


  
