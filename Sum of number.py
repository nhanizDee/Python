#Nhan Nguyen
#Date: feb 27, 2023
# Sum of number
# declare variable
number = 1.0
total = 0.0

while number > 0:
    number= float(input('Enter a positive number. Enter a negative number to quit.'))

    if number > 0.00:
        total += number
        
print('Totla equal to= ', format(total, '.2f'))



#n SUM i (i=1)  == n(n+1)/2

#factoral 1
number = 0
while number<=0:
    number= int(input('Enter a non negative integer:'))
    factorial = 1
for fac in range(1, number+1):
    factorial *= fac
print('The facto of', number, 'is', factorial)
print(factorial)

    
#factorial 2- simple than 1 and less condition to check
number= int(input('Enter the nonnegative number:'))
factorial =1

for i in range(1,number+1):
    factorial *= i
print(factorial)

