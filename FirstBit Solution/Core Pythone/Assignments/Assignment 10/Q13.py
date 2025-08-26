### 13 . Write a program to print list after removing even numbers.

li = [10, 21, 30, 41, 50, 61, 70, 81, 90, 101]
new_list = []
for i in range(len(li)):
    if li[i] % 2 != 0:
        new_list.append(li[i])
print(f'List after removing even numbers:', new_list)