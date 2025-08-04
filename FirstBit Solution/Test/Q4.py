###  Calculate the cost of painting the following building’s walls (both interior and 
# exterior). You need to accept area (one wall) and cost of both interior and 
# exterior wall.

area = int(input("Enter the area of one wall: "))

interior_walls = int(input("Enter number of interior walls: "))
exterior_walls = int(input("Enter number of exterior walls: "))

interior_cost = int(input("Enter cost per square unit for interior walls: "))
exterior_cost = int(input("Enter cost per square unit for exterior walls: "))

total_interior_area = area * interior_walls
total_exterior_area = area * exterior_walls

total_interior_cost = total_interior_area * interior_cost
total_exterior_cost = total_exterior_area * exterior_cost

total_cost = total_interior_cost + total_exterior_cost

print(f"Total interior painting cost:{total_interior_cost} \nTotal exterior painting cost: {total_exterior_cost} \nTotal painting cost: {total_cost}")
