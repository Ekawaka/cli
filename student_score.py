# Write a python program that allows the user to enter the score of a student and assigns a grade from A to E

score = int(input("enter score:"))
grade = ""

if score > 90:
    grade = "A"

elif score > 70 < 90:
    grade = "B"

elif score > 50 < 70:
    grade = "C"

elif score > 30 < 50:
    grade = "D"

elif score > 20:
    grade = "E"

    print(grade)
    print (score)
