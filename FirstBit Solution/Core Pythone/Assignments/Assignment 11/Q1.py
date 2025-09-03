# 1. WAP Python Program to Put Even and Odd elements of a List into two Different Lists.
def separate_even_odd(input_list):
    even_list = []
    odd_list = []
    
    for num in input_list:
        if num % 2 == 0:
            even_list.append(num)
        else:
            odd_list.append(num)
    
    return even_list, odd_list

input_list = [10, 21, 4, 45, 66, 90, 93]
even_list, odd_list = separate_even_odd(input_list)
print("Even List:", even_list)
print("Odd List:", odd_list)

