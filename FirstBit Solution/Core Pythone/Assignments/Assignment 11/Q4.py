# 4. Python Program to Find the Second Largest Number in a List Using Bubble Sort.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def find_second_largest(arr):
    if len(arr) < 2:
        return None  
    sorted_arr = bubble_sort(arr)
    return sorted_arr[-2] 

numbers = [12, 35, 1, 10, 34, 1]
second_largest = find_second_largest(numbers)
if second_largest is not None:
    print("The second largest number is:", second_largest)
else:
    print("List must contain at least two distinct numbers.")
