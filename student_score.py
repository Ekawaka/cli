# Write a python program that allows the user to enter the score of a student and assigns a grade from A to E

score = int(input("enter score:"))
grade = ""

if (score >= 80):
    grade = "A"

elif (score >= 60):
    grade = "B"

elif (score >= 50):
    grade = "C"

elif (score >= 40):
    grade = "D"

elif (score >= 30):
    grade = "E"

    print(grade)
