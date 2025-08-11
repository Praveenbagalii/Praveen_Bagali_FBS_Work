### WAP to print all numbers in a range divisible by a given number. 
num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))
divisor = int(input("Enter the divisor: "))
for i in range(num1, num2 + 1):
    if i % divisor == 0:
        print(i, end=" ")