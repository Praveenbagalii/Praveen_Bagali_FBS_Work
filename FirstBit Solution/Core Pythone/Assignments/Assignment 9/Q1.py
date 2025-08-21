# 1. Write a program to find sum of following series using recursive functions:  
# i. 1! + 2!  + 3! + 4! +….. + n!  
# Note : For fact and sum two recursive functions

def fact(n):
    if (n == 0):
        return 1
    else:
        return n * fact(n - 1)
    
def sumFact(n):
    if (n == 0):
        return 0
    else:
        return fact(n) + sumFact(n - 1)
        
n = int(input("Enter the number:"))
sumFactorial = sumFact(n)
print(f'The sum of 1! + 2!  + 3! + 4! +…..+{n}! is {sumFactorial} ')