### 6. Write a program to remove duplicates from the list.

li = [10, 20, 30, 40, 50, 10, 20, 30]
new_list = []
for i in range(len(li)):
    if li[i] not in new_list:
        new_list.append(li[i])
print("List after removing duplicates:", new_list)
