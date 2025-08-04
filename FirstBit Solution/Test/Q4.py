# Calculate the cost of painting the following building’s walls (both interior and 
# exterior). You need to accept area (one wall) and cost of both interior and 
# exterior wall.  
# (Note: 1. Below diagram is of two joint rooms. 
# 2. It is upper view of building.)


area = int(input("Enter area of one wall: "))
interior_cost = int(input("Enter cost per square unit for interior walls: "))
exterior_cost = int(input("Enter cost per square unit for exterior walls: "))

total_interior_walls = 4 + 4 - 2  # one shared interior wall = -2 interior surfaces
total_exterior_walls = 4 + 4 - 1  # one shared exterior wall = -1 exterior surface

total_interior_area = total_interior_walls * area
total_exterior_area = total_exterior_walls * area

interior_total_cost = total_interior_area * interior_cost
exterior_total_cost = total_exterior_area * exterior_cost

total_cost = interior_total_cost + exterior_total_cost

print(f"\nTotal painting cost is: {total_cost}")
