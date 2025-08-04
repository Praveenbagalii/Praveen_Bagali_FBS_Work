###  Write a program to check if person is eligible to marry or not (male age >=21 and 
# female age>=18) 

gender = input("Enter Gender (Male/Female):")
age = int(input("Enter Age:"))

if ((gender == "Female" and age >= 18) or (gender == "Male" and age >= 21)):
    print("Eligible for Marriage")
else:
    print("Not Eligible for Marriage")