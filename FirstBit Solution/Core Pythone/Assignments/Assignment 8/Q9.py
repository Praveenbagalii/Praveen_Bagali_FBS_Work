### 9. Write a program to check if entered number is a palindrome or not

def PalindromeNumber(num):
    temp = num
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10
    
    if num == rev:
        print(f'{num} is a Palindrome number.')
    else:
        print(f'{num} is not a Palindrome number.')


n = int(input("Enter a number: "))
PalindromeNumber(n)

