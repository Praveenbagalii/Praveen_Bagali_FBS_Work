### Find the area and parimeter

l = int(input("Enter length: "))
r = int(input("Enter radius: "))
b = 2 * r  # breadth = diameter

area = (l * b) + (0.5 * 3.14 * r * r)   # Area = rectangle area + semicircle area

peri = l + (2 * r) + (3.14 * r)  # Perimeter = length + diameter + semicircle circumference

print(f'Area is {area} and Perimeter is {peri}')
