current_price = 140
previous_price = 200
decrease = float(100*((previous_price-current_price)/previous_price))

if decrease >=10:
  print(f'the current price is {current_price} and the previous price is {previous_price}, the price is decreased by {decrease}% Buy this product!')  