import queue

def rev(text):
    wynik = ""
    cos = queue.LifoQueue()
    for i in text:
     cos.put(i)
     
    while not cos.empty(): 
      wynik = wynik + cos.get() 
    
    return wynik

print(rev('dupA'))