import os


class User:
    def __init__(self, name, age, email, phone_number):
        self.name = name
        self.age = age
        self.email = email
        self.__phone_number = phone_number

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Email: {self.email}\n' \
               f'Phone Number: {self.__phone_number}\n\n'


path = os.getcwd()

flag = True
while flag:
    choice = input("1. Add user\n"
                   "2. View users\n"
                   "3. Delete all users\n"
                   "4. Copy the image's data to text file\n"
                   "5. Write 'Hello' to image to corrupt the image\n"
                   "6. Restore the original image data to the original file\n"
                   "7. Duplicate image data from the copied image data\n"
                   "Enter the choice: ")
    file = open(path + '\\User Details\\userdetails.txt', 'a+')
    match choice:
        case '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            email = input("Enter email: ")
            phone_number = input("Enter phone number: ")
            user = User(name, age, email, phone_number)
            file.write(user.__str__())
            file.close()

        case '2':
            with open(path + '\\User Details\\userdetails.txt', 'r') as user_details:
                print(user_details.read())

        case '3':
            file.close()
            file = open(path + '\\User Details\\userdetails.txt', 'w')
            file.write('')
            print("Data cleared...")

        case '4':
            with open(path + '\\User Details\\download.jfif', 'rb+') as img_details:
                img = img_details.read()
                print(img)
                img_file = open(path + '\\User Details\\download.txt', 'rb+')
                img_file.write(img)
                img_file.close()

        case '5':
            with open(path + '\\User Details\\download.jfif', 'wb+') as img_details:
                img_details.write(b'Hello')

        case '6':
            with open(path + '\\User Details\\download.txt', 'rb+') as img_details:
                img = img_details.read()
                img_file = open(path + '\\User Details\\download.jfif', 'wb+')
                img_file.write(img)
                img_file.close()

        case '7':
            with open(path + '\\User Details\\download.txt', 'rb+') as img_details:
                img = img_details.read()
                img_file = open(path + '\\User Details\\python.jfif', 'wb+')
                img_file.write(img)
                img_file.close()

        case _:
            flag = False
