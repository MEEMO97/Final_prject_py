import uuid

# TODO 1 Enter your name and submission date
my_name = "Mohammed Salama Attaallah"
delivery_date = 23 - 8 - 2023


# TODO 2 Define Course Class and define constructor with


class Course:
    courses = []

    def __init__(self):
        self.course_id = uuid.uuid4()
        self.course_name = input("Enter course name")
        self.course_mark = input("Enter course mark")
        Course.courses.append([self.course_id, self.course_name, self.course_mark])


class Student:
    # TODO 3 define static variable indicates total student count
    student_counts = 0

    # TODO 4 define a constructor which includes

    def __init__(self, name, age, number):
        self.student_id = uuid.uuid4()
        self.student_name = name
        self.student_age = age
        self.student_number = number
        Student.student_counts += 1
        self.student_courses = []

    # TODO 5 define a method to enroll new course to student courses list
    def enroll_courses(self, course_id):
        ids = [i for i, n, m in Course.courses]
        for index, x in enumerate(ids):
            if course_id == x:
                return self.student_courses.append(Course.courses[index])

    # method to get_student_details as dict
    def get_student_details(self):
        return self.__dict__

    # method to get_student_courses
    def get_student_courses(self):
        # TODO 6 print student courses with their marks
        for index, i in enumerate(self.student_courses):
            print(self.student_courses[index][1:])

    # method to get student_average as a value
    def get_student_average(self):
        # TODO 7 return the student average
        mark_sum = 0
        for index, i in enumerate(self.student_courses):
            mark_sum += self.student_courses[index][2]
        return mark_sum / len(self.student_courses)


# in Global Scope
# TODO 8 declare empty students list
students = []
while True:

    # TODO 9 handle Exception for selection input
    try:
        selection = int(input("1.Add New Student\n"
                              "2.Delete Student\n"
                              "3.Display Student\n"
                              "4.Get Student Average\n"
                              "5.Add Course to student with mark.\n"
                              "6.Exit"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    if selection == 1:
        student_number = input("Enter Student Number")
        student_name = input("Enter Student Name")
        while True:
            try:
                student_age = int(input("Enter Student Age"))
                break
            except:
                print("Invalid Value")

        # TODO 10 create student object and append it to students list
        student = Student(student_name, student_age, student_number)
        print("Student Added Successfully")

    elif selection == 2:
        student_number = input("Enter Student Number")
        # TODO 11 find the target student using loops and delete it if exist , if not print ("Student Not Exist")

    elif selection == 3:
        student_number = input("Enter Student Number")
        # TODO 12 find the target student using loops and print student detials  if exist , if not print ("Student Not Exist")

    elif selection == 4:
        student_number = input("Enter Student Number")
        # TODO 13 find the target student using loops and get student average  if exist , if not print ("Student Not Exist")

    elif selection == 5:
        student_number = input("Enter Student Number")
        # TODO 14 ask user to enter course name and course mark then create coures object then append it to target student courses

    else:
        # TODO 15 call a function to exit the program
        pass
