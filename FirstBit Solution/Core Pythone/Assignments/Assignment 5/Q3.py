### Accept no. of passengers from user and per ticket cost. Then accept age of each  
# passenger and then calculate total amount to ticket to travel for all of them based on  
# following condition : 
### a. Children below 12 = 30% discount 
## b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full.

num_passengers = int(input("Enter number of passengers: "))
ticket_cost = int(input("Enter ticket cost per passenger (Rs): "))

total_amount = 0

for i in range(1, num_passengers + 1):
    age = int(input(f"Enter age of passenger {i}: "))
    
    if age < 12:                  # Children discount 30%
        price = ticket_cost * 0.7
    elif age > 59:              # Senior citizen discount 50%
        price = ticket_cost * 0.5
    else:                        # No discount
        price = ticket_cost
    
    print(f"Ticket price for passenger {i}: Rs.{price:}")
    total_amount += price

print(f"\nTotal ticket amount for all passengers: Rs.{total_amount:}")
