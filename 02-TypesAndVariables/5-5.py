price = float(input("price="))
discount = float(input("discount="))
price_with_discount = float(price - price*discount/100)
change = float(price-price_with_discount)

print(f'price of product is {price:.2f}. the doscount is {discount:.2f}. the price with discount is {price_with_discount:.2f}. the disserence of prices is {change:.2f}')

