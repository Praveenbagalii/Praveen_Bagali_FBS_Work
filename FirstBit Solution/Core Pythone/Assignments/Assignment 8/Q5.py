### 5. Sum of all prime numbers between 1 to n 

def CheckPrime(num):
    if num < 2:   
        return False
    for i in range(2, num // 2 + 1):   
        if num % i == 0:
            return False
    else:
        return True

def sum_of_primes(n):
    total = 0
    for i in range(2, n + 1):  
        if CheckPrime(i):
            total += i
    return total

n = int(input("Enter a number (n): ")) 
print(f"Sum of all prime numbers between 1 and {n} is: {sum_of_primes(n)}")
