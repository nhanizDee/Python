def future_value(p, i, t):
    return p * (1 + i / 100) ** t


# get user input
present_value = float(input("Enter current bank balance:"))
interest_rate = float(input("Enter interest rate:"))
months = int(input("Enter the amount of time that passes:"))

# calculate and print future value
future = future_value(present_value, interest_rate, months)
print(future)

p: float = float(input("Enter current bank balance:"))
i = float(input("Enter interest rate:"))
t = float(input("Enter the amount of time that passes:"))
f = p * pow((1 + i), t)
print(f)
