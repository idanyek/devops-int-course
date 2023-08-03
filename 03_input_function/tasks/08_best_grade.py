num1, num2, num3, num4, num5 = map(int,input("please enter 5 grades from 1 to 100, sepereted by space: ").split())

print("best grade is: ", max(num1,num2,num3,num4,num5))

best_grade = num1
if (num2 > best_grade):
    best_grade = num2
if (num3> best_grade):
    best_grade = num3
if (num4 > best_grade):
    best_grade = num4
if (num5 > best_grade):
    best_grade = num5

print("best grade is: ", best_grade)

#or
print("best grade is: ", max(list(map(int,input("please enter grades from 1 to 100, sepereted by space: ").split()))))