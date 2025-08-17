### 2. Write a program to calculate area of circle

def circle_area(radius):
    return 3.14 * radius * radius

r = float(input("Enter the radius of the circle: "))

area = circle_area(r)
print("The area of the circle is:", area)
