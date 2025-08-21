### 4. Write a program to find sum of n numbers using recursion.
def sos(n):
    if (n == 0):
        return 0
    else:
        return n + sos(n - 1)
    
num = int(input("Enter the number:"))
sum = sos(num)
print(f'The sum of 1 to {num} is {sum}')