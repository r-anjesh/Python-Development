student_hieghts = input("Input a list of student hieght").split()

for n in range(0,len(student_hieghts)):
    student_hieghts[n] = int(student_hieghts[n])

print(student_hieghts)
sum = 0
count = 0
for i in student_hieghts:
    sum += i
    count += 1
print(round(sum/count))
