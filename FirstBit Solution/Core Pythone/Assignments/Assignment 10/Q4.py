### 4. Write a program to reverse the list.

li = [10, 20, 30, 40, 50]
rev_list = []

for i in range(len(li)-1, -1, -1): 
    rev_list.append(li[i])

print("Original List:", li)
print("Reversed List:", rev_list)


