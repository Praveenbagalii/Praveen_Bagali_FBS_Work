emp = int(input("Enter the number of employees: "))
total_salary_of_all = 0  

for i in range(1, emp + 1):
    salary = int(input(f"Enter the basic salary for employee {i}: "))

    if salary < 20000:
        da = salary * 10/100
        ta = salary * 12/100
        hra = salary * 15/100
    else:
        da = salary * 15/100
        ta = salary * 18/100
        hra = salary * 20/100

    total_salary = salary + da + ta + hra
    print(f"Total salary of employee {i}: {total_salary}")

    total_salary_of_all += total_salary 

print(f"Total salary of all {emp} employees = {total_salary_of_all}")
