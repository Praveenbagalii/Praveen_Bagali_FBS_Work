#Percentage of student based on marks of 5 subjects
m1 = int(input("subject 1 Mark: "))
m2 = int(input("subject 2 Mark: "))
m3 = int(input("subject 3 Mark: "))
m4 = int(input("subject 4 Mark: "))
m5 = int(input("subject 5 Mark: "))

Total_gain_marks = m1 + m2 + m3 + m4 + m5
percentage = (Total_gain_marks/ 500) * 100 

print(f'Percentage is {percentage}%.') 