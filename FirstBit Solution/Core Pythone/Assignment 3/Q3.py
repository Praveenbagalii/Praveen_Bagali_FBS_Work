### Write a program to input angles of a triangle and check whether triangle is valid or not.
a = int(input("Enter First Angle:"))
b = int(input("Enter Second Angle:"))
c = int(input("Enter Third Angle:"))
if (a + b + c == 180):
    print("This triangle is valid")
else:
    print("This is not valid")
