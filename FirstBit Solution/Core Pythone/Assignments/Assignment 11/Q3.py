# 3. Python Program to Sort the List According to the Second Element in Sublist.

def sort_by_second_element(input_list):
    # Using bubble sort to sort the list based on the second element of each sublist
    n = len(input_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if input_list[j][1] > input_list[j+1][1]:
                # Swap if the second element is greater
                input_list[j], input_list[j+1] = input_list[j+1], input_list[j]
    return input_list
input_list = [[1, 3], [3, 2], [5, 1], [4, 4]]
sorted_list = sort_by_second_element(input_list)
print("List sorted by second element:", sorted_list)

