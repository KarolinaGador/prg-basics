class c:
    def __init__(self, punkty):
        self.punkty = punkty
    def m(self, n):
     counter = 0
     for listy in self.punkty:
        if listy[0] >0 and listy[1]>0:
           counter = counter + 1  
     if counter>=n:
        return True
     else:
        return False
def main():     
 cos = c([[2,3],[1,8],[-6,4],[3,-7]])
 print(cos.m(2)) 
 print(cos.m(3))

if __name__ == "__main__":
 main()