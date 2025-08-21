### 9. Write a program to calculate the m to the power n using recursion.

def power(m, n):
    if n == 0:              
        return 1
    else:
        return m * power(m, n - 1)   

m = int(input("Enter base (m): "))
n = int(input("Enter exponent (n): "))

result = power(m, n)
print(f"{m}^{n} = {result}")

