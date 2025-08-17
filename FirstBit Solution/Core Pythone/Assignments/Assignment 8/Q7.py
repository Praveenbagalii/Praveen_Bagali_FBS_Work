### 7. Write a program to find sum of digits of a number. 

def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10   
        total += digit
        num = num // 10   
    return total

n = int(input("Enter a number: "))
print(f"Sum of digits of {n} is: {sum_of_digits(n)}")
