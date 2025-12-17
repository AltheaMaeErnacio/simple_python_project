print("=== Student Grade Evaluator ===")

name = input("Enter student name: ")
grade = float(input("Enter your grade: "))

if grade >= 75:
    print("Congratulations,", name + "!")
    print("You passed with a grade of", grade)
else:
    print("Sorry,", name + ".")
    print("You failed with a grade of", grade)