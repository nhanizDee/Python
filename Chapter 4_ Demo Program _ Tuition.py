tuition = 8000

print(f"Current semester tuition: {tuition:.2f}")


tuition = 8000  # initial tuition amount

for year in range(1, 6):
    tuition *= 1.03  # increase tuition by 3% each year
    print(f"In {year} year{'s' if year > 1 else ''}, the tuition will be ${tuition}.")





