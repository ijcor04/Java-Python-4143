#Isaiah Corrales
#Program 5, CMPS-4143-102
#November 6th, 2024
import re
grades_dict = {}
search = r"([A-Za-z]+ [A-Za-z]+): ([\d, ]+)"

with open("input.txt", "r") as file:
    for line in file:
       
       match = re.search(search, line.strip())
       if match:
           # Extract name and grades
           name = match.group(1)
           grades = match.group(2).split(",")
           # Strip extra whitespace from grades and convert to integers
           grades = [int(grade.strip()) for grade in grades]
           # Save to the dictionary 
           grades_dict[name] = grades

   

    n = 6
    ent = 0
    while (ent != n):
        print("\n\n")
        print("MENU\n")
        print("1. Add a Student\n")
        print("2. Add one or more grades\n")
        print("3. View grades of a student and their average\n")
        print("4. View all students and grades\n")
        print("5. Save updates in a file\n")
        print("6. to exit\n")
        ent = int(input("Please enter your choice: "))

        match ent:

             case 1:
               
                new_student = input("Please enter the student's name followed by grades (ex, 'Isaiah Corrales: 89, 90, 91, 92, 93.): ")
                match = re.search(r"([A-Za-z ]+):\s*([\d, ]+)\.", new_student.strip())
                if match:
                  name = match.group(1).strip()
                  grades = [int(x) for x in match.group(2).split(',')]
                  grades_dict[name] = grades
                  print(f"Grades for {name}: {grades}")
                else:
                   print("Incorrect\n")
             case 2:
                
                temp_grades = input("Please enter the student's name followed by grades (ex, 'Patrick Star: 98, 99, 98, 96, 95.): ")
                match = re.search(r"([A-Za-z ]+):\s*([\d, ]+)\.",temp_grades.strip())
                if match:
                   name = match.group(1).strip()
                   grades = [int(x) for x in match.group(2).split(',')]
                   
                   if name in grades_dict:
                      
                      grades_dict[name].extend(grades)
                      print(f"Grades for {name}", grades_dict[name])
                   else:
                      
                      grades_dict[name] = grades
             case 3:
                stu_name = input("Please enter the name of the student: ")
                match = re.search(r"([A-Za-z ]+)",stu_name.strip())
                if match:
                   
                   name = match.group(1).strip()
                   temp_grades = grades_dict.get(name)

                   if temp_grades:
                  
                     print(f"Grades for {name}:")
                     for grade in temp_grades:
                        print(grade)
                     
                     average = sum(temp_grades) / len(temp_grades)
                     print(f"Average grade for {name}: {average:.2f}")
                   else:
                     print(f"There are no grades recorded for {name}.\n")
                else:
                   print("There is no student by that name.\n")
                   
             case 4:
                for name, grades in grades_dict.items():
                    print (f"{name}: {grades}")
             case 5:
                file_name = input("Please enter the name of the file you would like to save to(ex, 'output.txt'): ")
                with open(file_name, "w") as file:
                   for name, grades in grades_dict.items():
                      
                      grades_line = f"{name}: {', '.join(map(str, grades))}\n"
                      file.write(grades_line)
                   print(f"Grades have been saved to {file_name} \n")  
             
               

            
            

        
        
        
