class c:
    def __init__(self, name, surname, age, seniority):
        self.name = name
        self.surname= surname
        self.age = age
        self.seniority = seniority

    def __str__(self):
        if self.age<18:
          return f'{self.surname.lower()}{self.name[0].lower()}{str(self.seniority)}'
        else:
          return f'{self.surname.upper()}{self.name[0]}{str(self.seniority)}'

print(str(c("Szymon", "Kądzielawa", 19, 1)))      # maya7
print(str(c("Karolina", "Gądor", 19, 0)))  # BROWNG4          

