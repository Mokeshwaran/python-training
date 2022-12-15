from collections import deque, namedtuple


class Member:
    member_details = deque(maxlen=5)

    def __init__(self, name='name', email='email', address='address'):
        self.name = name
        self.email = email
        self.address = address

    def set_last_member(self, name='name', email='email', address='address'):
        self.member_details.append([name, email, address])

    def set_first_member(self, name='name', email='email', address='address'):
        self.member_details.appendleft([name, email, address])

    def get_member_details(self):
        return self.member_details


member = Member()
flag = True
while flag:
    choice = input("1. Add Member\n"
                   "2. View Member\n"
                   "3. Add First Member\n"
                   "4. Remove Last Member\n"
                   "5. Remove First Member\n"
                   "6. Rotate Members\n"
                   "Enter your choice: ")

    match choice:
        case '1':
            print("NOTE: Only 5 members will be added, if additional members are to be"
                  " added then the initial member will be removed")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            member.set_last_member(name, email, address)

        case '2':
            print(member.get_member_details())

        case '3':
            print("NOTE: Only 5 members will be added, if additional members are to be"
                  " added then the final member will be removed")
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            member.set_first_member(name, email, address)

        case '4':
            print("Removing the last member")
            print(member.get_member_details().pop())

        case '5':
            print("Removing the first member")
            print(member.get_member_details().popleft())

        case '6':
            print("Rotating the members for work, first 3 will work.")
            member.get_member_details().rotate(3)
            # Negative values results in reverse rotation and default value is 1.

        case _:
            flag = False


# Usually Deque is used in case of time based activities like
# 1. Browser History.
# 2. Weather Forecast
# 3. Real-time Stock Markets.
# 4. and Other Real-time Stats.
