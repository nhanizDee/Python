num= int(input("Enter a nonegative integer: "))
factorial = 1
# loop and condition
for i in range(1, num+1):
    factorial *= i
print(factorial)
