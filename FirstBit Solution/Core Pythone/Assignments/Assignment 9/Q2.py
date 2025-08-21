# 2. Write a program to check if given number is Armstrong or not using recursive function. 

def count_digits(num):
    if num == 0:
        return 0
    else:
        return 1 + count_digits(num // 10)

def power_sum(num, power):
    if num == 0:
        return 0
    else:
        digit = num % 10
        return (digit ** power) + power_sum(num // 10, power)

def is_armstrong(num):
    digits = count_digits(num)
    if num == power_sum(num, digits):
        return True
    else:
        return False

n = int(input("Enter a number: "))
if is_armstrong(n):
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is Not an Armstrong number.")
