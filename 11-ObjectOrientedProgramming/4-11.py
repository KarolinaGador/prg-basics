class C:
    def __init__(self, stadion):
        self.stadion = stadion
    def m1(self,s,n):
        self.stadion[s]=n
    def m2(self,s):
        suma =0
        for sectors in s:
            if sectors in self.stadion:
             suma = suma + self.stadion[sectors]
        return suma

def main():
 cos =C({"A":120,"D":150,"G":90,"K":110})
 print(cos.m1("G",130))
 print(cos.m2("GD"))
 print(cos.m2("KEJ"))  
if __name__ == "__main__":
  main()  

