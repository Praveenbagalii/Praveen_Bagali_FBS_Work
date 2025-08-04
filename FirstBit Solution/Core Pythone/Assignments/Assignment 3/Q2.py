### Write a program to input any alphabet and check whether it is vowel or consonant.
a = input("Enter The Alphabet:")
if (a in 'aeiouAEIOU'):
    print(f'{a} is Vowel')
else:
    print(f'{a} is Consonant')
