### 8. Write a program to create a duplicate of an existing list. It should not point to
# same list.
li = [10, 20, 30, 40, 50, 10, 20, 30]
new_list = []
for i in range(len(li)):
    new_list.append(li[i])
print("Original List:", li)
print("Duplicate List:", new_list)


# old_list = [10, 20, 30, 40]
# new_list = old_list[:]   

# new_list.append(50)   
# print("Old List:", old_list)
# print("New List:", new_list)
