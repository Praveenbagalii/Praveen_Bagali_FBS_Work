### Write a program to check whether the triangle is equilateral, isosceles or scalene 
# triangle.
a = int(input("Enter First Angle:"))
b = int(input("Enter Second Angle:"))
c = int(input("Enter Third Angf:"))
if a == b and b == c:
    print("This is an Equilateral triangle")
elif a == b or b == c or a == c:
    print("This is an Isosceles triangle")
else:
    print("This is a Scalene triangle")