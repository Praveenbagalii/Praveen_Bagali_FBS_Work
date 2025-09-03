# 8. Print 1 to 100 in snakes and ladder pattern. 

def print_snakes_and_ladders(n):
    for i in range(n):
        if i % 2 == 0:
            
            for j in range(1, n + 1):
                print(i * n + j, end="\t")
        else:
            
            for j in range(n, 0, -1):
                print(i * n + j, end="\t")
        print()  
print_snakes_and_ladders(10)
