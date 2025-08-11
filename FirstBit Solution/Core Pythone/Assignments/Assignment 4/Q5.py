### WAP to print Fibonacci series upto n. 
num = int(input("Enter the number: "))
a = -1
b = 1

while a < num:
    temp = a + b  
    print(a, end=" ")

    a = b          
    b = temp      


