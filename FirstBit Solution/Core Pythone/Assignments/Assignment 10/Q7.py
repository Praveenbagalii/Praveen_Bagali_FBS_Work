###7. Write a program to create a new list from existing list which contains cube of
# each number of list.
li = [1, 2, 3, 4, 5]
cube_list = []
for i in range(len(li)):
    cube_list.append(li[i] ** 3)
print("List with cubes of each element:", cube_list)