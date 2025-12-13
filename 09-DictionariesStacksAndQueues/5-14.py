import queue

kolejka = queue.Queue()
number = 0  

while True:
    wybor = input("Nowy klient przychodzi-1, klient odchodzi-2, 3-koniec: ")

    if wybor == '1':
        number += 1            
        kolejka.put(number)   
        print(f'Klient z biletem #{number} dodany do kolejki.')

    elif wybor == '2':
        if not kolejka.empty():
            o = kolejka.get()
            print(f'Klient z biletem #{o} został obsłużony.')
        else:
            print('Kolejka jest pusta.')

    elif wybor == '3':
        print("Koniec programu.")
        break

    else:
        print("Niepoprawny wybór. Wpisz 1, 2 lub 3.")
