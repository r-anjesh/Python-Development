student_marks = input("Enter a list of a marks of student : ").split()
for x in range(0,len(student_marks)):
    student_marks[x] = int(student_marks[x])
print(student_marks)
maxi = 0
for x in student_marks:
    if maxi < x:
        maxi = x

print(f'The highest marks in the class is : {maxi}')