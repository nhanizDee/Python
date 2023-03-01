# Date: Feb 1, 2023
# Nhan Nguyen

#Buy                                            Sell
# share :2000                                   2000* 42.75
# price / share: $40                             
# broken =(2000*40)/ (3/100)                     (lay tren * 3.75)
# comm :$82400                                    lay 82400- cai tren

#Constant
PURCHASE_PRICE = 40.00
SELLING_PRICE = 42.75
NUMBER_OF_SHARE = 2000
COMMISSION_RATE =  0.03


# VARIABLE
amt_paid_for_stock = 0.00
commission_purchase = 0.00
total_paid =  0.00

amt_recieved_for_selling = 0.00
commission_selling = 0.00
total_amt_received_selling = 0.00

profit_loss =0.00

## Buying Part
# calculate the amount paid while buying
amt_paid_for_stock = NUMBER_OF_SHARE * PURCHASE_PRICE

# amount of commmision
commission_purchase = amt_paid_for_stock * COMMISSION_RATE

# total paid for buying
total_paid = amt_paid_for_stock + commission_purchase

## Selling Part
# amount received for selling
amt_recieved_for_selling = NUMBER_OF_SHARE * SELLING_PRICE

# commission from selling the share
commission_selling = amt_recieved_for_selling * COMMISSION_RATE

# total for selling
total_amt_received_selling = amt_recieved_for_selling + commission_selling

# profit/loss
profit_loss = total_paid - total_amt_received_selling


## Display part

print("Amount paid for stock: $", format(amt_paid_for_stock, '.2f'))

print("Commission buy: $", format(commission_purchase, '.2f'))

print("Amount for selling: $", format(amt_recieved_for_selling, '.2f'))

print("Commission received while selling: $", format(commission_selling, '.2f'))

print("Profit or lost after the process: $", format(profit_loss, '.2f'))











