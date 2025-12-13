import queue

exp = input('Enter RPN expression (e.g. 23+5*): ')
operacja = queue.LifoQueue()

for i in exp:
    if i.isdigit():  # jeśli znak jest cyfrą
        operacja.put(int(i))
    elif i in '+-*/':  # jeśli znak jest operatorem
        b = operacja.get()
        a = operacja.get()
        
        if i == '+':
            operacja.put(a + b)
        elif i == '-':
            operacja.put(a - b)
        elif i == '*':
            operacja.put(a * b)
        elif i == '/':
            operacja.put(a / b)
    elif i == '=':  # znak końca wyrażenia
        wynik = operacja.get()
        print("Wynik:", wynik)
        break