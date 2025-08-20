### WAP Check given number is palidrom or not using recursion

def reverse(num, rev=0):
    if num == 0:  
        return rev
    else:
        rev = (rev * 10) + (num % 10)   
        return reverse(num // 10, rev)  

def palindrome(num): 
    if num == reverse(num):
        return True
    else:
        return False

n = int(input("Enter a number: "))
if palindrome(n):
    print(f"{n} is a Palindrome number.")
else:
    print(f"{n} is NOT a Palindrome number.")
