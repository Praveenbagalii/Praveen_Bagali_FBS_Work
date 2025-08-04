###  Write a program to check if user has entered correct userid and password.
user_name = "Praveen"
password= "123456"

a = input("Enter The User ID:")
b = input("Enter The Password:")

if (user_name == a) and (password == b):
    print("Login is Successful")
    
else:
    print("Invaild User ID or Password")