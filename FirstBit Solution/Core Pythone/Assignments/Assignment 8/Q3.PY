# 3. Write a program to find sum of following series using functions :
# a. 1+ 2 + 3 + 4+..... + n
# b. 1!+ 2! + 3! + 4!+..... + n!
# c. 1^1 + 2^2 + 3^3+ ...... n^n

# a) 1 + 2 + ... + n
def sum_natural(n):
    return n * (n + 1) // 2   
    
# b) Sum of factorials: 1! + 2! + ... + n!
def sum_factorials(n):
    total = 0
    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i + 1):
            fact *= j   
        total += fact
    return total

# c) Sum of powers: 1^1 + 2^2 + ... + n^n
def sum_powers(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** i
    return total

# Main program
n = int(input("Enter a number (n): "))

print(f"a) Sum of first {n} numbers: {sum_natural(n)}")
print(f"b) Sum of factorials up to {n}!: {sum_factorials(n)}")
print(f"c) Sum of series (1^1 + 2^2 + ... + {n}^{n}): {sum_powers(n)}")
