### c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
n = int(input("Enter n: "))
sum_geometric = 0
for i in range(n):
    sum_geometric += 2 ** i 
print(f"The sum of the geometric series from 1 to {n} with a common ratio of 2 is: {sum_geometric}")


### explaination with example
# The geometric series is calculated as follows:
# 1 + 2^1 + 2^2 + ... + 2^(n-1)
# For example, if n = 5, the series would be:
# 1 + 2 + 4 + 8 + 16 = 31