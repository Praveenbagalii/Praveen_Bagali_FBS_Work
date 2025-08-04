### Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition : 
# a. Children below 12 = 30% discount 
# b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full. 
age1 = int(input("Enter the 1st people age: "))
age2 = int(input("Enter the 2nd people age: "))
age3 = int(input("Enter the 3rd people age: "))
age4 = int(input("Enter the 4th people age: "))
age5 = int(input("Enter the 5th people age: "))
tic_amt = int(input("Enter the ticket price: "))


if (age1 < 12):
    dis_amt = tic_amt * 0.3
    total_amt1 = tic_amt - dis_amt
elif(age1 > 59):
    dis_amt = tic_amt * 0.5
    total_amt1 = tic_amt - dis_amt
else:
    total_amt1 = tic_amt

if (age2 < 12):
    dis_amt = tic_amt * 0.3
    total_amt2 = tic_amt - dis_amt
elif(age2 > 59):
    dis_amt = tic_amt * 0.5
    total_amt2 = tic_amt - dis_amt
else:
    total_amt2 = tic_amt

if (age3 < 12):
    dis_amt = tic_amt * 0.3
    total_amt3 = tic_amt - dis_amt
elif(age3 > 59):
    dis_amt = tic_amt * 0.5
    total_amt3 = tic_amt - dis_amt
else:
    total_amt3 = tic_amt

if (age4 < 12):
    dis_amt = tic_amt * 0.3
    total_amt4 = tic_amt - dis_amt
elif(age4 > 59):
    dis_amt = tic_amt * 0.5
    total_amt4 = tic_amt - dis_amt
else:
    total_amt4 = tic_amt

if (age5 < 12):
    dis_amt = tic_amt * 0.3
    total_amt5 = tic_amt - dis_amt
elif(age5 > 59):
    dis_amt = tic_amt * 0.5
    total_amt5 = tic_amt - dis_amt
else:
    total_amt5 = tic_amt

total_amt = total_amt1 + total_amt2 + total_amt3 + total_amt4 + total_amt5
print(f'The total amount is {total_amt}')
