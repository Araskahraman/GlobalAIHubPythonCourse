

def get_info():
    name = str(input("Please enter a student name"))
    midgrade = float(input("Please enter midgrade"))
    project = float(input("Please enter project grade"))
    final = float(input("Please enter final grade"))
    
    return name,midgrade,project,final

def convert(name,midgrade,project,final):
    student_info = {"name":name,"midgrade":midgrade,"project":project,"final":final}
    
    return student_info

def calculate_passing_grade():
     total_grade = student_info["midgrade"]*(0.3) + student_info["project"]*(0.3) + student_info["final"]*(0.4)


student_info_tuple = get_info()
print(student_info_tuple)

student_info_dict = convert(*student_info_tuple)
print(student_info_dict)

passing_grade = calculate_passing_grade(get_info())
print(passing_grade)


