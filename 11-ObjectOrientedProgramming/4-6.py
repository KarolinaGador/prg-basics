import bank

def main():
    ktos = bank.konto()
    ktos.create('12 3456 5555 9090 1111 0000 7722')
    ktos.wplac(56)
    ktos.status()
    ktos.wyplac(100)
    ktos.status()
if __name__ == "__main__":
    main()   