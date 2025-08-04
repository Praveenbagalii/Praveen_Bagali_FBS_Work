### Write a program to swap two numbers without using third variable. 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num1, num2 = num2, num1
print(f'After swapping:  first number = {num1}, second number = {num2}')