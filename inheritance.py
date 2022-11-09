class Person(object):
    """This is the class for Person."""
    def __init__(self, name, age):
        """
        This is the constructor for class Person.

        :param name: Name of the person.
        :param age: Age of the person.
        """
        self.name = name
        self.age = age

    def display_details(self):
        """
        This will display the details of a Person like
        person's name and person's age.
        """
        return f'Name: {self.name}\nAge: {self.age}'


class Employee(Person):
    """This Employee class is inherited from the Person class."""
    def __init__(self, employee_id,
                 name, age, salary):  # Line break for readability.
        self.employee_id = employee_id
        self.salary = salary
        super().__init__(name, age)

    def display_employee_details(self):
        """
        This method will display the details of the employee.
        :return: Employee Details
        """
        return f'ID: {self.employee_id}\n' + super().display_details() \
               + f'\nSalary: {self.salary}'


class Company(Person):
    """This is the class of Company"""
    def __init__(
            self, company_id, name,
            age, company_location):  # Hanging indent for readability.
        self.company_id = company_id
        self.company_location = company_location
        super().__init__(name, age)

    def display_company_details(self):
        return f'Company ID: {self.company_id}\n' + super().display_details()\
               + f'\nCompany Location: {self.company_location}'


employee_1 = Employee(13, 'Moki', 23, 25000)
print(employee_1.display_employee_details())

company_1 = Company(1, 'e-Company', 12, 'Chennai')
print(company_1.display_company_details())
