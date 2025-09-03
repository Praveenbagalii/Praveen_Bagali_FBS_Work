# 10. Write a program to print list after removing even numbers without using inbuilt.

def remove_even_numbers(input_list):
    result_list = []
    for num in input_list:
        if num % 2 != 0:  
            result_list.append(num)
    return result_list
input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original List:", input_list)
output_list = remove_even_numbers(input_list)
print("List after removing even numbers:", output_list)
