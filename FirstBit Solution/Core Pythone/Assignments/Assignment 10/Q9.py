### 9. Write a program of having n number of elements in the list and find out even
# and odd elements in that list and then create two separate lists which will have
# even elements and other will have odd elements.

li = [10, 21, 32, 43, 54, 65, 76, 87, 98]
even_list = []
odd_list = []
for i in range(len(li)):
    if li[i] % 2 == 0:
        even_list.append(li[i])
    else:
        odd_list.append(li[i])
print(f'Even List: {even_list}')
print(f'Odd List: {odd_list}')