from collections import namedtuple

n = int(input())
columns = input().split()
Student = namedtuple("Student", columns)
students = []

for i in range(n):
    row = input().split()
    students.append(Student(*row))

total = 0
for student in students:
    total += int(student.MARKS)

print("{:.2f}".format(total / n))
