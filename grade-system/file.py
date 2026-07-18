# grade_system.py

try:
    mark = float(input("Enter the student's mark (0-100): "))

    if mark < 0 or mark > 100:
        print(f"Invalid mark: {mark}. Marks must be between 0 and 100.")
    else:
        if mark >= 90:
            grade = "A"
        elif mark >= 80:
            grade = "B"
        elif mark >= 70:
            grade = "C"
        elif mark >= 60:
            grade = "D"
        elif mark >= 50:
            grade = "E"
        else:
            grade = "F"

        print(f"Entered mark: {mark}")
        print(f"Grade: {grade}")

except ValueError:
    print("Invalid input. Please enter a numeric value between 0 and 100.")