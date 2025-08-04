#Compound Interest
P = int(input("Enter Principal: "))
T = int(input("Enter Time in years: "))
R = int(input("Enter Rate of Interest: "))

CI = (P * (1 + R/100) ** T) - P

print(f'Compound Interest is {CI}.')