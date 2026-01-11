class Phone():
    def __init__(self, dzwonic, kolor):
        self.dzwonic = dzwonic
        self.kolor = kolor
        self.marka = 'Xiaomi'
        self.wlaczony = True
    def wlaczanie(self):
        self.wlaczany = True
    def wylaczanie(self):
        self.wlaczony = False
    def info(self):
        print(f'Marka to {self.marka}, kolor to {self.kolor}, czy jest wlaczony {self.wlaczony}')
        print(f'dzwonimy do {self.dzwonic}')  
def main():
    tel = Phone("Do Ali", "Czarny")
    tel.wylaczanie()
    tel.info()
if __name__ =="__main__":
    main()   
                
        
