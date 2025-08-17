# 1 2 3 4 5 
# 2     5
# 3   5
# 4 5
# 5

for i in range(1, 6):
    for j in range(1, 6):
        if i == 1:                       
            print(j, end=" ")
        elif j == 1:                     
            print(i, end=" ")
        elif i + j == 6:                 
            print(5, end=" ")
        else:
            print("  ", end="")          
    print()
