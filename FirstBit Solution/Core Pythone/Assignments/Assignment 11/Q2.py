# 2. Python Program to Merge Two Lists and Sort.
def merge_and_sort(list1, list2):
    merged_list = list1 + list2
    merged_list.sort()
    return merged_list

list1 = [5, 2, 9, 1]
list2 = [6, 3, 8, 4]
sorted_list = merge_and_sort(list1, list2)
print("Merged and Sorted List:", sorted_list)