### A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing 
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle 
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total 
# cost of fencing the field.

r = 20
length = 50
breadth = 40
cost_per_meter = 35
fencing_times = 5
 
half_circle = 3.14 * r  # π * r length of the semicircle

rectangle_sides = 2 * length + breadth

total_length = half_circle + rectangle_sides

fencing_length = total_length * fencing_times

total_cost = fencing_length * cost_per_meter

print(f"Total cost of fencing the field is {total_cost}")
