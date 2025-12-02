# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   counter = 0
   for row in cinema_seats:
      for miejsce in row:
         counter = counter + 1

   return counter

def seats_available(seats):
   counter = 0
   for row in cinema_seats:
      for miejsce in row:
         if miejsce=='A':
          counter = counter + 1
   return counter

def seats_booked(seats):
   counter = 0
   for row in cinema_seats:
      for miejsce in row:
         if miejsce=='B':
          counter = counter + 1
   return counter

def seat_status(seats, row, place):
   a = cinema_seats[row-1][place-1]
   if a=='A':
    return 'Avalible'
   elif a =='B':
      return 'Booked'
         

print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats,1,1))
print('Seat in row 5, place 5:', seat_status(cinema_seats,5,5))
print('Seat in row 3, place 5:', seat_status(cinema_seats,3,5))