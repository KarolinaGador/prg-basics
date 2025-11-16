products = int(input('Enter number of products: '))
price = int(input('Enter the price: '))

#In one of the online stores, a 25% discount is charged for each product purchased over two. Write a program that calculates the amount to be paid.

if products >= 0 and products<=2:
    total = price * products
    print(f'the price is {total}')
elif products > 2:
    total = (2 * price) +  (products-2)* 0.75*price
    print(f'the price is {total}')
else:
    print('invalid data')