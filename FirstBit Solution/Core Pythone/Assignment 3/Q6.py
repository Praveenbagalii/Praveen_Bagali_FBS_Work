### Write a program to calculate profit or loss.
cp = int(input("Enter Cost Price: "))
sp = int(input("Enter Selling Price: "))
if sp > cp:
    print(f"Profit")
elif sp < cp:
    print(f"Loss")
else:
    print("Neutral")