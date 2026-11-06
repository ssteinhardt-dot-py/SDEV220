# Name: Samuel Steinhardt

# App Name: Module_2_Lab.py

# This program accepts user inputs last name, first name, and GPA
# This will use a while loop and if statements to determine whether 
# a student has made the honor roll or the Dean's list


# This is the priming input for the loop. This should be compared 
# until user enters ZZZ
student_l_name = input("Please input student's last name (or ZZZ to quit): ")



# Using .lower() makes it easier to quit the loop by making ZZZ 
# not case-sensitive

# This while loop will continue untill zzz in some form has been entered
while student_l_name.lower() != 'zzz':
    student_f_name = input("Please enter student's first name: ")
    # We all float down here...
    gpa = float(input("Please enter the student's GPA: "))
    if gpa >= 3.5:
        print(student_f_name, student_l_name, "has made the dean's list!")
    
    # I was unsure if I should use an elif here, as the assignment does 
    # not specify if the student can be on the honor roll and the Dean's 
    # list at the same time. If they cant, this line be be fixed by using 
    # elif instead, so I just assumed that the student can do both. 
    if gpa >= 3.25:
        print(student_f_name, student_l_name, "has made the honor roll!")

    # We need to ask for the last name again to prevent an infinite loop 
    student_l_name = input("Please input student's last name (or ZZZ to quit): ")