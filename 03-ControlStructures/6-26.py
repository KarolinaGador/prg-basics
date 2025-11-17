pin = "1234"
guess = input("Enter your pin: ")
tries = 0


while tries <3:

  if pin == guess:
      print("Correct pin")
      break
  else:
      tries += 1
      print("pin incorrect")
  if tries == 3:
            print("Sorry, too many tries")
            break

  guess = input("Enter your pin: ")     
     