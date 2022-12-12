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


# class Employee(object):
#     emp_id = 0
#
#     def __init__(self, emp_id, name):
#         self.emp_id = emp_id
#         self.name = name
#
#     def __str__(self):
#         return f"ID: {self.emp_id}\n" \
#                f"Name: {self.name}"
#
#
# class Trainee(Employee):
#     def __init__(self, course, duration, emp_id, name):
#         super().__init__(emp_id, name)
#         self.course = course
#         self.duration = duration
#
#     def __str__(self):
#         return f"{super().__str__()}\n" \
#                f"Course: {self.course}\n" \
#                f"Duration: {self.duration}"
#
#
# class Trainer(Employee):
#     def __init__(self, training_experience, training_course, emp_id, name):
#         super().__init__(emp_id, name)
#         self.training_experience = training_experience
#         self.training_course = training_course
#
#     def __str__(self):
#         return f"{super().__str__()}\n" \
#                f"Experience in training: {self.training_experience}\n" \
#                f"Preferred course for training: {self.training_course}"
#
#
# emp_id = Employee.emp_id
# flag = True
# while flag:
#     choice = int(input("Choose any one\n"
#                        "1. Trainee\n"
#                        "2. Trainer\n"
#                        "or press any number to exit...\n"))
#     match choice:
#         case 1:
#             name = input("Name: ")
#             course = input("Course: ")
#             duration = input("Duration (in days): ")
#             emp_id += 1
#             trainee = Trainee(emp_id=emp_id, name=name, course=course, duration=duration)
#             print(trainee, end="\n")
#
#         case 2:
#             name = input("Name: ")
#             training_exp = input("Experience in training (in years): ")
#             training_course = input("Training course: ")
#             emp_id += 1
#             trainer = Trainer(emp_id=emp_id, name=name, training_experience=training_exp,
#                               training_course=training_course)
#             print(trainer, end="\n")
#         case _:
#             flag = False

class Instruments:
    def __init__(self, units, title, color):
        # super(Instruments, self).__init__(units, title, color)
        self.units = units
        self.title = title
        self.color = color

    @staticmethod
    def is_available(units):
        return units > 0

    def __str__(self):
        return f"Units: {self.units}\n" \
               f"Title: {self.title}\n" \
               f"Color: {self.color}"


class Manufacturer:
    def __init__(self, name, description, location):
        # super(Manufacturer, self).__init__(name, description, location)
        self.name = name
        self.description = description
        self.location = location

    def __str__(self):
        return f"Manufacturer name: {self.name}\n" \
               f"Manufacturer description: {self.description}\n" \
               f"Manufacturer Location: {self.location}\n"

#
# class Woodwinds(Instruments):
#     def __init__(self, units, title, color, tone_holes, mouthpiece):
#         super().__init__(units, title, color)
#         self.tone_holes = tone_holes
#         self.mouthpiece = mouthpiece
#
#     def __str__(self):
#         return f"{super().__str__()}\n" \
#                f"Tone Holes: {self.tone_holes}\n" \
#                f"Mouthpiece: {self.mouthpiece}"
#
#
# class Strings(Instruments):
#     def __init__(self, units=0, title='strings', color='color', string_number=0, string_type='string_type'):
#         super().__init__(units, title, color)
#         self.string_number = string_number
#         self.string_type = string_type
#
#     def __str__(self):
#         return f"{super().__str__()}\n" \
#                f"Number of strings: {self.string_number}"


class Percussion(Instruments, Manufacturer):
    def __init__(self, units, title, color, diameter, name, description, location):
        # super().__init__()
        Instruments.__init__(self, units, title, color)
        Manufacturer.__init__(self, name, description, location)
        self.diameter = diameter

    def __str__(self):
        return f"{Instruments.__str__(self)}\n" \
               f"{Manufacturer.__str__(self)}" \
               f"Diameter: {self.diameter}"


print(Percussion(10, "Timpani", "Brass", 10, "The", "Company", "Location"))