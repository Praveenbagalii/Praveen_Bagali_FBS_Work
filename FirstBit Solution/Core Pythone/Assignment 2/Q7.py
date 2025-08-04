### Find the sum of three-digit number.
number = int(input("Enter a three-digit number: "))
sum_of_digits = (number // 100) + ((number // 10) % 10) + (number % 10)
print(f'The sum of the digits in {number} is: {sum_of_digits}')  