#Find Third Angle of a Triangle
angle1 = int(input("Enter first angle: "))
angle2 = int(input("Enter second angle: "))

angle3 = 180 - (angle1 + angle2)

print(f'Third angle of triangle is {angle3}.')