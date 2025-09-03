# 5. Python Program to Sort a List According to the Length of the Elements within the list. 
def sort_by_length(input_list):
    # Using bubble sort to sort the list based on the length of each element
    n = len(input_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if len(input_list[j]) > len(input_list[j+1]):
                # Swap if the length of the current element is greater
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return input_list

input_list = ["apple", "banana", "kiwi", "cherry", "blueberry", "fig"]
sorted_list = sort_by_length(input_list)
print("List sorted by length of elements:", sorted_list)
