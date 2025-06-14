gpa = []
def calculate_gpa(grade, type):
    if type == "Regular":
        if grade >= 97:
            return 4.0
        elif grade >= 93:
            return 3.8
        elif grade >= 90:
            return 3.6 
        elif grade >= 87:
            return 3.4
        elif grade >= 83:
            return 3.2
        elif grade >= 80:
            return 3.0
        elif grade >= 77:
            return 2.8
        elif grade >= 73:
            return 2.6
        elif grade >= 70:
            return 1.4
        elif grade < 70:
            return 0.0
        else:
            return 0.0
    elif type == "Honors":
        if grade >= 97:
            return 4.5
        elif grade >= 93:
            return 4.3
        elif grade >= 90:
            return 4.1
        elif grade >= 87:
            return 3.9
        elif grade >= 83:
            return 3.7
        elif grade >= 80:
            return 3.5
        elif grade >= 77:
            return 3.3
        elif grade >= 73:
            return 3.1
        elif grade >= 70:
            return 2.9
        elif grade < 70:
            return 0.0
        else:
            return 0.0
    elif type == "AP":
        if grade >= 97:
            return 5.0
        elif grade >= 93:
            return 4.8
        elif grade >= 90:
            return 4.6
        elif grade >= 87:
            return 4.4
        elif grade >= 83:
            return 4.2
        elif grade >= 80:
            return 4.0
        elif grade >= 77:
            return 3.8
        elif grade >= 73:
            return 3.6
        elif grade >= 70:
            return 3.4
        elif grade < 70:
            return 0.0
        else:
            return 0.0
    else:
        raise ValueError("Invalid grade type")

# Read the grades.csv file if it exists
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
grades_file = os.path.join(script_dir, 'grades.csv')
import csv
if os.path.exists(grades_file):
    print("Reading Grades...")
    with open(grades_file, mode='r') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header row
        for row in reader:
            if len(row) == 2:
                grade, gradeType = row  
                gpa.append(calculate_gpa(float(grade), gradeType))
# If the file does not exist, prompt the user for grades
else:
    print("No previous grades found. Please enter your grades.")
    # Loop to get grades from the user
    while True:
        gradeType = input("Enter the type of the next grade (Regular/Honors/AP)(Type anything else to stop): ").strip()
        #exit loop if user types anthing other than Regular, Honors, or AP
        if gradeType not in ["Regular", "Honors", "AP"]:
            break
        grade = float(input("Enter your next grade: "))
        gpa.append(calculate_gpa(grade, gradeType))
        

print("Calculating GPA...")

print(f"Your GPA is: {sum(gpa) / len(gpa):.2f}")
