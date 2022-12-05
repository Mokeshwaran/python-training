class Student:
    """
    This class contains the details of the students.
    (e.g): Name, Age, Email, Address.
    """
    def __init__(self, name, age, email, address):
        self.name = name
        self.__age = age
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\n" \
               f"Email: {self.email}\n" \
               f"Address: {self.address}"

    def student_age(self):
        """
        This method shows the age of the student.

        :return: Student's age.
        """
        return f"Age: {self.__age}"


s = Student("Mokesh", 23, "mokesh@i2i.com", "222/697")

print(s)
print(s.address)
# print(s.__age)
print(s._Student__age)  # Using name mangling to access the age attribute from Student.
s._Student__age = 19
print(s.student_age())
