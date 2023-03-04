#team member
#Nhan Nguyen
#Cochise Nava
#Max Raven
#Date: Feb 22, 2023 


# Declare Variables Constants for car, rate, monthly compound, time



CAR = 45575.25

r = 0.02675

m = 12

t = 5

# Variables for the 2 options



i = r / m

n = m * t

IncentiveA = CAR - 6000

IncentiveB = CAR



# PMT Equation

# PMT = PV*(i/ (1-(1+i)**-n))



# Calculation for Incentive A



# Amount paid per month with Incentive A with interest

PMT_A = IncentiveA *(i/(1-(1+i)**-n))



# Amount paid per month with Incentive A if there was no interest

## Do this to find how much interest we are paying per month, and 5 years

PMT_A1 = IncentiveA / n



# Total Amount paid per month with the duration of 5 years

## Payment per month * total months

totalA = PMT_A * n



# Interest paid per month

## Payment with interest - Payment with no interest

IPM_A = PMT_A - PMT_A1



# total interest paid for Incentive A,

## Payment with interest - Payment with no interest * total months

IPM_A1 = (PMT_A - PMT_A1) * n



## Amount saved with condition A

##CAR payment - payment with condition A

MSA = CAR - totalA



# Calculation for Incentive B



# Amount paid per month with Incentive B with interest

PMT_B = IncentiveB / n



# Amount paid per month with Incentive B if there was no interest

## Do this to find how much interest we are paying per month, and 5 years

PMT_B1 = IncentiveB / n



# Total Amoung paid per month with the duration of 5 years

## Payment per month* total months

totalB = PMT_B * n



# Interest paid per month

## Payment with interest - Payment with no interest

IPM_B = PMT_B - PMT_B1



# total interest paid for Incentive B

## Payment with interest - Payment with no interest * total months

IPM_B1 =(PMT_B - PMT_B1) * n



# Amount saved with condition B

## CAR payment - payment with condition B

MSB = CAR - totalB



# Print output from our inputs

print("PMT for Incentive A: $", format(PMT_A, '.2f'))          

print("PMT for Incentive B: $", format(PMT_B, '.2f'))

          

print("Interest per month for Incentive A: $", format(IPM_A, '.2f'))          

print("Interest per month for Incentive B: $", format(IPM_B, '.2f'))



print("Total Interest for Incentive A: $", format(IPM_A1, '.2f'))          

print("Total Interest for Incentive B: $", format(IPM_B1, '.2f'))

          

print("Money saved over five years for Incentive A: $", format(MSA, '.2f'))         

print("Money saved over five years for Incentive B: $", format(MSB, '.2f'))

