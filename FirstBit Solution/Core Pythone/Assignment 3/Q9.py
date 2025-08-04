### Input 5 subject marks from user and display grade(eg.First class,Second class ..)
a = int(input("Enter marks for subject 1: "))
b = int(input("Enter marks for subject 2: "))
c = int(input("Enter marks for subject 3: "))
d = int(input("Enter marks for subject 4: "))
e = int(input("Enter marks for subject 5: "))
total_marks = a + b + c + d + e
percentage = (total_marks / 500) * 100
if percentage >= 80:
    print("Grade: First Class")
elif percentage >= 60:
    print("Grade: Second Class")
elif percentage >= 40:
    print("Grade: Third Class") 
else:
    print("Grade: Fail")

