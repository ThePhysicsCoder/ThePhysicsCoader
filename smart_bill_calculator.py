
#smart bill calculator
print('welcome to smart bill calculator!')
items=[]
prices=[]
while True:
    item=input('enter product name (type done to finish): ')
    if item.lower()=='done':
       break
    price=float(input(f'enter the price of {item}: Rs '))
    items.append(item)
    prices.append(price)


#subtotal calculation
subtotal=float(sum(prices))
print(f"\nyour subtotal amount is: Rs {subtotal:.2f}")


#ask for tax percentage,discount, delivery charge
tax_in_percent=float(input('\nenter tax percentage(8 for 8%): '))
discount_in_percent=float(input('enter your discount percentage(8 for 8 %): '))
delivery=float(input('enter delivery charge: Rs '))
tax=tax_in_percent/100*subtotal
discount=discount_in_percent/100*subtotal
final_bill_amount=subtotal+tax-discount+delivery

print('-----------------------------------------------')
print('\n-----final bill details----')
for i in range(len(items)):
    print(f'{items[i]}: Rs {prices[i]}')

print(f'\nyour subtotal amount:Rs {subtotal}')
print(f"your discount percent is {discount_in_percent}%: Rs {discount:.2f}")
print(f"your tax percentage is {tax_in_percent}%: Rs {tax:.2f}")
print(f'your delivery charge amount is Rs {delivery}')
print(f'your final bill amount is {final_bill_amount:.2f}' )
