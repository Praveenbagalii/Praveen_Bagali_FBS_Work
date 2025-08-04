### Write a program to prompt user to enter userid and password. After verifying 
# userid and password display a 4 digit random number and ask user to enter the 
# same. If user enters the same number then show him success message otherwise 
# failed. (Something like captcha) 
import random

user_name = "Praveen"
password= "123456"

a = input("Enter The User ID:")
b = input("Enter The Password:")

if (user_name == a) and (password == b):
    print("Login Successful")

    catcha = random.randint(1000,9999)
    print(f'Catcha Number:{catcha}')

    user_catcha = int(input("Enter the Catcha:"))

    if (catcha == user_catcha):
        print("Success")
    else:
        print("Faild")

else:
    print("Invaild User ID or Password")