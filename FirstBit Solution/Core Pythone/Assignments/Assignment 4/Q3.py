### WAP to print sum of series upto n. 
num = int(input("Enter the number: "))
sum_series = 0
for i in range(1, num + 1):
    sum_series += i 
print(f'Sum of series from 1 to {num} is: {sum_series}')