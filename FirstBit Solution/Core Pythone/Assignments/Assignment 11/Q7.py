# 7. Python Program to Find the Intersection of Two Lists without using inbuilt.
def intersection_of_lists(list1, list2):
    intersection_list = []
    for item in list1:
        if item in list2 and item not in intersection_list:
            intersection_list.append(item)
    return intersection_list

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = intersection_of_lists(list1, list2)
print("Intersection of the two lists:", result)