#This is the priming input for the loop. This should be compared 
#until user enters ZZZ
student_l_name = input("Please input student's last name (or ZZZ to quit): ")


while student_l_name.lower() != 'zzz':
    student_f_name = input("Please enter student's first name: ")
    gpa = float(input("Please enter the student's GPA: "))
    if gpa >= 3.5:
        print(student_f_name, student_l_name, "has made the dean's list!")
    if gpa >= 3.25:
        print(student_f_name, student_l_name, "has made the honor roll!")
    student_l_name = input("Please input student's last name (or ZZZ to quit): ")