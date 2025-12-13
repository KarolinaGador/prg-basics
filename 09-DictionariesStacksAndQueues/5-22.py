import json

# read product data from keyboard
name = input('Enter name of the product: ')
price = float(input("Enter price: "))
paid = input('Is it paid y/n: ')=='y'

product = {}

product['name'] = name
product["price"] = price
product['paid']= paid

with open('product.json', "w") as file:
    json.dump(product, file, indent=4)