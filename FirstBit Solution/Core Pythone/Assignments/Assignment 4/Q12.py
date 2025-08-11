### WAP to print Armstrong number within a given range 
num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))

for num in range(num1, num2 + 1):
    power = len(str(num))  # number of digits
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    if total == num:
        print(num, end=" ")