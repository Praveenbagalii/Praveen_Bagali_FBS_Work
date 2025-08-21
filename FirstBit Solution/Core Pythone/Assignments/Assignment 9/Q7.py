### 7. Write a program to find sum of digits using recursion. 

def sod(n):
    if (n == 0):
        return 0
    else:
        return (n % 10) + sod(n // 10)

n = int(input("Enter the number:"))
sum = (sod(n))
print(sum)
