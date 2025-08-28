### 11. Write a program to print all numbers which are divisible by m and n in the list.

li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
m = int(input("Enter The m number:"))
n = int(input("Enter The n number:"))
divisible_list = []
for i in range(len(li)):
    if li[i] % m == 0 and li[i] % n == 0:
        divisible_list.append(li[i])
print(f'Numbers divisible by {m} and {n}:', divisible_list)
