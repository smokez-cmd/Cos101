

student_name = input("Student name: ")
coursework = float(input("Coursework score (out of 30): "))
examination = float(input("Examination score (out of 70): "))

if coursework < 0 or coursework > 30 or examination < 0 or examination > 70:
    print("Invalid input")
else:
    total = coursework + examination

    if total >= 70:
        grade = "A"
    elif total >= 60:
        grade = "B"
    elif total >= 50:
        grade = "C"
    elif total >= 45:
        grade = "D"
    elif total >= 40:
        grade = "E"
    else:
        grade = "F"

    if total >= 50:
        decision = "Pass"
    else:
        decision = "Resit required"

    print("\nSTUDENT RESULT SUMMARY")
    print("Name:", student_name)
    print("Coursework:", coursework, "/ 30")
    print("Examination:", examination, "/ 70")
    print("Total:", total, "/ 100")
    print("Grade:", grade)
    print("Decision:", decision)
