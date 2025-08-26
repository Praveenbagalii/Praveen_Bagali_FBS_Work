### 3. Write a program to find the second largest element in the list.
li = [10, 20, 30, 40, 50]
maxi = li[0]
second_maxi = 0
for i in range(len(li)):
    if li[i] > maxi:
        second_maxi = maxi
        maxi = li[i]
    elif li[i] > second_maxi:
        second_maxi = li[i]
print("Second Largest:", second_maxi)