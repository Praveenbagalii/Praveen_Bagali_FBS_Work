# Convert distance given in feet and inches into meters and remaining centimeters
feet = int(input("Enter distance in feet: "))
inches = int(input("Enter distance in inches: "))

total_inches = (feet * 12) + inches
total_meters = total_inches * 0.0254

meters = int(total_meters)
remaining_centimeters = (total_meters - meters) * 100

print(f'Distance is {meters} meters and {remaining_centimeters} centimeters.')

