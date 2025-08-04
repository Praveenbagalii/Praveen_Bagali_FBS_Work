### Write a program to accept an integer amount from user and tell minimum 
# number of notes needed for representing that amount.
amount = int(input("Enter Amount:"))
n2000 = amount//2000
amount = amount % 2000

n500 = amount//500
amount = amount % 500

n200 = amount//200
amount = amount % 200

n100= amount//100
amount = amount % 100

n50 = amount//50
amount = amount % 50

n20 = amount//20
amount = amount % 20

n10 = amount//10
amount = amount % 10

n5 = amount//5
amount = amount % 5

n2 = amount//2
amount = amount % 2

n1 = amount//1

total = n2000+n500+n200+n100+n50+n20+n10+n5+n2+n1

print (f'Total Number Of Notes is {total}.')
