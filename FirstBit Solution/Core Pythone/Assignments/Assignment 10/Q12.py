### 12. Write a program to create three lists of numbers, their squares and cubes

li = [1, 2, 3, 4, 5]
square_list = []
cube_list = []
for i in range(len(li)):
    square_list.append(li[i] ** 2)
    cube_list.append(li[i] ** 3)
print(f'Original List: {li}')
print(f'Square List: {square_list}')
print(f'Cube List: {cube_list}')