### 10. Write a program to remove all occurrences of a given element in the list.
li = [10, 20, 30, 40, 50, 10, 20, 30]
remove = 20
new_list = []
for i in range(len(li)):
    if li[i] != remove:
        new_list.append(li[i])
print(f'List after removing all occurrences of {remove}:', new_list)