import random
class termometr:
    def __init__(self):
        self.temp = 36
        self.stat = ""
        self.on = False
        
    def oon(self):
        self.on = True
    def oof(self):
        self.on = False    
    def measure(self):
       if self.on ==True: 
        self.temp = round(random.uniform(34, 42), 1)    
        if self.temp >37.0 and self.temp<41.0:
           self.stat = "(fever)"
        elif self.temp>=41.0:
           self.stat ="CRITICAL" 
        else:
           self.stat = ""   
    def info(self):
       print(f'temperature {self.temp} {self.stat}')       

           