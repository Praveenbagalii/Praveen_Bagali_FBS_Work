### Find the area and parimeter

l = int(input("Enter length: "))
b = int(input("Enter breadth: "))
r = int(input("Enter redius: "))

area = (l * b) + (0.5 * 3.14 * r * r)
peri = 2 * (l + r) + (3.14 * r)

print(f'Area is {area} and Perimeter is {peri}')