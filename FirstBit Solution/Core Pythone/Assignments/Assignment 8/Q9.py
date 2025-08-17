### 9. Write a program to check if entered number is a palindrome or not

def reverse_number(num):
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    return rev

def is_palindrome(num):
    reversed_num = reverse_number(num)  
    return num == reversed_num          

n = int(input("Enter a number: "))
result = is_palindrome(n)   

if result:
    print(f"{n} is a palindrome number.")
else:
    print(f"{n} is not a palindrome number.")
