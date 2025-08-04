### Write a program to input all sides of a triangle and check whether triangle is valid or 
#not.
a = int(input("Enter First Side:"))
b = int(input("Enter Second side:"))
c = int(input("Enter Third side:"))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("This triangle is valid")
else:
    print("This is not valid")