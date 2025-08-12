### Write a program to prompt user to enter userid and password. If Id and  
## password is incorrect give him chance to re-enter the credentials. Let him try 3  
# times. After that program to terminate.
id = "Praveen"
Pass = "123456"

for attempt in range(3):
    userid = input("Enter User ID: ")
    password = input("Enter Password: ")

    if userid == id and password == Pass:
        print("Login Successful!")
        break
    else:
        print("Invalid credentials. Try again.")
else:
    print("Too many failed attempts. Access Denied.")
