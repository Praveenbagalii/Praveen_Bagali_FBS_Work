### WAP to check if given number Strong Number. 

num = int(input("Enter the number:"))
temp = num
sum = 0

while(temp > 0):
    d = temp % 10
    temp = temp //10

    i = 1
    fact = 1 
    while(i <= d):
        fact *= i
        i += 1

    sum += fact

if(sum == num):
    print(f'{num} is a strong number')
else:
    print(f'{num} is a not strong number')