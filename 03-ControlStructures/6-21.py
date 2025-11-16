pln = int(input("Enter the amount in PLN: "))
tpln = 0
opln =0
fpln=0

if pln<2:
 opln = pln



if pln<5:
 tpln = pln//2
 remi = pln%2
 if remi>0:
    opln=remi



if pln>=5:
    fpln = pln//5
    remi = pln%5
    if remi>=2:
        tpln = remi//2
        remi = remi%2
        if remi>0:
            opln = remi

print(f' 5pln coins {fpln} 2pln coins {tpln} 1pln coins {opln}')           