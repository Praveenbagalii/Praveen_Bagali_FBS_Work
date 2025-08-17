### 1. Write a program to calculate area of rectangle

def rectangle_area(length, width):
    return length * width

l = int(input("Enter the length of the rectangle: "))
w = int(input("Enter the width of the rectangle: "))

area = rectangle_area(l, w)
print("The area of the rectangle is:", area)
