### 8. Write a program to check whether a number is prime or not using recursion.

def is_prime(num, divisor=2):
    if num <= 1:
        return False
    if divisor > num // 2:   
        return True
    if num % divisor == 0:   
        return False
    
    return is_prime(num, divisor + 1)

n = int(input("Enter a number: "))
if is_prime(n):
    print(f"{n} is a Prime number.")
else:
    print(f"{n} is NOT a Prime number.")
