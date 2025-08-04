###  Write a program to reverse three-digit number.
number = int(input("Enter a three-digit number: "))
hundreds = number // 100
tens = (number // 10) % 10
units = number % 10
reversed_number = (units * 100) + (tens * 10) + hundreds
print(f'The reversed number is: {reversed_number}')