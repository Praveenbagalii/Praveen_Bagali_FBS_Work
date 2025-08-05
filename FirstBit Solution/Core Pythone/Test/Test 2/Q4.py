### Write a program to calculate the total cost of painting. The interior of building with four 
# equal sized walls.
hight = int(input("Enter the height of the wall in meters: "))
width = int(input("Enter the width of the wall in meters: "))
cost_per_square_meter = int(input("Enter the cost of painting per square meter: "))
area = 4 * (hight * width)
total_cost = area * cost_per_square_meter
print(f"The total cost of painting the walls is: {total_cost}")

 
