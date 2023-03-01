#Nhan Nguyen
#feb,15,2023
# Software_Sales

#Constant
RETAIL_PRICE = 99.00

#declaire variable
quantity_orders =0
full_price = 0.00
discount_rate = 0.00 #could be double or float
disount_amount = 0.00
total_amount = 0.00


#code
quantity_orders = int(input('Enter the number of order: '))

if quantity_orders >99:
    discount_rate = 0.40
elif quantity_orders > 49:
    discount_rate = 0.30
elif quantity_orders > 19:
    discount_rate = 0.20
elif quantity_orders > 9:
    discount_rate = 0.10
else: discount_rate =0.00

full_price= RETAIL_PRICE * quantity_orders

disount_amount= discount_rate * full_price

total_amount=full_price - disount_amount

print('You got discount of $', format(disount_amount ,'.2f'))
print('Total for you is $' , format(total_amount, '.2f'))
    
