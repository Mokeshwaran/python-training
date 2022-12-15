from collections import defaultdict


def default_value():
    return "No Staff Found"


class Staff:
    staff = defaultdict(default_value)
    staff_id = 0
    staff_id += 1

    def __init__(self, name='name', dob='10-10-2000', email='email@email.com',
                 ph_number='9876543210'):
        self.name = name
        self.__dob = dob
        self.email = email
        self.ph_number = ph_number

    def set_staff(self, name, dob, email, ph_number):
        self.staff[self.staff_id] = [name, dob[6: 10], email, ph_number]

    def get_staff(self, staff_id):
        return self.staff[staff_id]

    def get_staffs(self):
        print(self.staff.items())

    def del_staff(self, staff_id):
        self.staff.pop(staff_id)
        print("Staff Deleted")


staff = Staff()
flag = True
while flag:
    choice = input("1. Add\n"
                   "2. View\n"
                   "3. View All\n"
                   "4. Delete\n"
                   "Choose your choice: ")
    match choice:
        case '1':
            name = input("Enter Name: ")
            dob = input("Enter Date Of Birth: ")
            email = input("Enter Email: ")
            ph_number = input("Enter Phone Number: ")
            staff.set_staff(name, dob, email, ph_number)
            print("Staff Added")

        case '2':
            staff_id = int(input("Enter Staff ID: "))
            print(staff.get_staff(staff_id))

        case '3':
            staff.get_staffs()

        case '4':
            s_id = int(input("Enter Staff ID:"))
            staff.del_staff(s_id)

        case _:
            flag = False
