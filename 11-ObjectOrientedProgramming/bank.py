class konto:
    def __init__(self):
      self.number = '11 1111 1111 1111 1111 1111 1111'
      self.balance = 0
    def create(self,acc):
       self.number = acc
    def wplac(self,kwota1):
       self.balance = self.balance + kwota1
    def wyplac(self,kwota2):
       if kwota2<=self.balance:
          self.balance = self.balance - kwota2
       else:
          print(f'za malo kasy ups')
    def status(self):
       print(f'number: {self.number}, balance: {self.balance}PLN')      
                  