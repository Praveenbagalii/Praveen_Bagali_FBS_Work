### WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))
for i in range(num1, num2 + 1):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=" ")