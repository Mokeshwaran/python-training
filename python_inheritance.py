# class Parent(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def details(self):
#         return f"Hello my name is {self.name}, my age is {self.age}"
#
#
# class Child(Parent):
#     def child_details(self):
#         return f"{super().details()} and I'm their child"
#
# child = Child("Moki", 17)
# print(child.child_details())
class Employee(object):
    emp_id = 0

    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def __str__(self):
        return f"ID: {self.emp_id}\n" \
               f"Name: {self.name}"


class Trainee(Employee):
    def __init__(self, course, duration, emp_id, name):
        super().__init__(emp_id, name)
        self.course = course
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Course: {self.course}\n" \
               f"Duration: {self.duration}"


class Trainer(Employee):
    def __init__(self, training_experience, training_course, emp_id, name):
        super().__init__(emp_id, name)
        self.training_experience = training_experience
        self.training_course = training_course

    def __str__(self):
        return f"{super().__str__()}\n" \
               f"Experience in training: {self.training_experience}\n" \
               f"Preferred course for training: {self.training_course}"


emp_id = Employee.emp_id
flag = True
while flag:
    choice = int(input("Choose any one\n"
                       "1. Trainee\n"
                       "2. Trainer\n"
                       "or press any number to exit...\n"))
    match choice:
        case 1:
            name = input("Name: ")
            course = input("Course: ")
            duration = input("Duration (in days): ")
            emp_id += 1
            trainee = Trainee(emp_id=emp_id, name=name, course=course, duration=duration)
            print(trainee, end="\n")

        case 2:
            name = input("Name: ")
            training_exp = input("Experience in training (in years): ")
            training_course = input("Training course: ")
            emp_id += 1
            trainer = Trainer(emp_id=emp_id, name=name, training_experience=training_exp,
                              training_course=training_course)
            print(trainer, end="\n")
        case _:
            flag = False
