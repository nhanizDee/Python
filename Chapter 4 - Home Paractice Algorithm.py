#Algorithm Workbench
#Nhan Nguyen
#Chapter 4


#work 1
# loop enter a number, number *10,
#then assign to variable "product" , iterate as long as product <100

product = 0
while product < 100:
    num = int(input('Enter an number: '))
    product = 10*num
    print(product)

#work 2
# loop ask user to enter two number
# add the two number and the sum displayed
# ask user if they want to do it again, if Y then repeat, orthwerise break