### a. 1! + 2! + 3! + 4! + …..n!
n = int(input("Enter a number to calculate the sum of factorials up to n: "))
factorial_sum = 0
for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    factorial_sum += fact
print(f"The sum of factorials from 1 to {n} is: {factorial_sum}")