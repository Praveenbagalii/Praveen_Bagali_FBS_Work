# 6. Python Program to Find the Union of two Lists without using inbuilt.
def union_of_lists(list1, list2):
    union_list = list1.copy()  # Start with all elements from the first list
    for item in list2:
        if item not in union_list:  
            union_list.append(item)
    return union_list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = union_of_lists(list1, list2)
print("Union of the two lists:", result)
