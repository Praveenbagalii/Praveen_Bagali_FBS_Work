### 5. Accept a number from user and check if this element is present in the list or
# not. Also tell how many times it is present in the list.

li = [10, 20, 30, 40, 50, 20, 30, 20]
num = int(input("Enter a number to check: "))
count = 0
for i in range(len(li)):
    if li[i] == num:
        count += 1
if count > 0:
    print(f"{num} is present in the list {count} times.")
else:
    print(f"{num} is not present in the list.")