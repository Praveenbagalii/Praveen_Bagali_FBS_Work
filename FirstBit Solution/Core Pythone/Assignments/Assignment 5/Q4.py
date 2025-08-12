### Write a program to check if given number is Armstrong number or not.  
## (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 + 4*4*4*4)

num = int(input("Enter a number: "))
power = len(str(num))        # number of digits
total = 0   
temp = num
while temp > 0:
    digit = temp % 10
    total += digit ** power
    temp //= 10
if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")