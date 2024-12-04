# Isaiah Corrales
# Program 5, CMPS-4143-102
# November 6th, 2024
#This program will read in a text file with pre-existing student names and grades,
#the program utilizes a dictionary to store the information, and there is a menu that has
# 5 options to choose from and operates on a sentinel loop/value.
import re

# Dictionary to store student grades
grades_dict = {}

# Regex pattern to match tab-separated names and grades
search = r"^([A-Za-z\s]+)\t([\d\t]+)$"

# Read and parse the input file
with open("grade.txt", "r") as file:
    for line in file:
        match = re.search(search, line.strip())
        if match:
            # Extract name and grades
            name = match.group(1).strip()
            grades = match.group(2).split("\t")
            # Convert grades to integers
            grades = [int(grade.strip()) for grade in grades]
            # Save to the dictionary
            grades_dict[name] = grades

# Menu-driven program
n = 6
ent = 0
while ent != n:
    print("\n\n")
    print("MENU\n")
    print("1. Add a Student\n")
    print("2. Add one or more grades\n")
    print("3. View grades of a student and their average\n")
    print("4. View all students and grades\n")
    print("5. Save updates in a file\n")
    print("6. Exit\n")
    ent = int(input("Please enter your choice: "))

    match ent:
        case 1:
            #case for adding a new student and their grades
            new_student = input("Enter the student's name followed by grades (e.g., 'Isaiah Corrales: 89, 90, 91, 92, 93'): ")
            match = re.search(r"([A-Za-z\s]+):\s*([\d,\s]+)", new_student.strip())
            if match:
                name = match.group(1).strip()
                grades = [int(x) for x in match.group(2).split(",")]
                grades_dict[name] = grades
                print(f"Grades for {name}: {grades}")
            else:
                print("Incorrect format.\n")
            
        case 2:
            #case for adding a grade(s) to an existing student
            temp_grades = input("Enter the student's name followed by grades (e.g., 'Patrick Star: 98, 99, 98, 96, 95'): ")
            match = re.search(r"([A-Za-z\s]+):\s*([\d,\s]+)", temp_grades.strip())
            if match:
                name = match.group(1).strip()
                grades = [int(x) for x in match.group(2).split(",")]
                if name in grades_dict:
                    grades_dict[name].extend(grades)
                    print(f"Updated grades for {name}: {grades_dict[name]}")
                else:
                    grades_dict[name] = grades
                    print(f"Grades added for new student {name}: {grades}")
        case 3:
            #case for viewing a students grade and their average
            stu_name = input("Enter the student's name: ")
            if stu_name in grades_dict:
                temp_grades = grades_dict[stu_name]
                print(f"Grades for {stu_name}: {temp_grades}")
                average = sum(temp_grades) / len(temp_grades)
                print(f"Average grade for {stu_name}: {average:.2f}")
            else:
                print(f"No grades recorded for {stu_name}.\n")
        case 4:
            #case for seeing all students and grades in the dictionary
            print("All Students and Grades:")
            for name, grades in grades_dict.items():
                print(f"{name}: {grades}")
        case 5:
            #case for saving the output to a file
            file_name = input("Enter the name of the file to save to (e.g., 'output.txt'): ")
            with open(file_name, "w") as file:
                for name, grades in grades_dict.items():
                    grades_line = f"{name}: {', '.join(map(str, grades))}\n"
                    file.write(grades_line)
            print(f"Grades have been saved to {file_name}.\n")
        case 6:
            #case for exiting!
            print("NOOOOOOOOOOOOOO!")
