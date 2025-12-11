import queue

number = 18

binary = queue.LifoQueue()
wynik=0
while number != 0:
 
 rem = number%2
 binary.put(rem)
 number = number//2
 print(binary.get())
