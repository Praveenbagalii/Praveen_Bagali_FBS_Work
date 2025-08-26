# 2. Write a program to find maximum and minimum element in a list.
li = [10, 20, 30, 40, 50]
maxi = li[0]
mini = li[0]
for i in range(len(li)):
    if li[i] > maxi:
        maxi = li[i]
    elif li[i] < mini:
        mini = li[i]
print("Maximum Number:", maxi)
print("Minimum Number:", mini)