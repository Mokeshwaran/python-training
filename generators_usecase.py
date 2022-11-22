def user_details(details):
    users.append(details)
    return users


def generate_id():
    for i in range(10000):
        yield i + 1


def show_users():
    for i in users:
        yield i


users = []
usrs = show_users()
flag = True
while flag:
    print("Enter username, 1 to show users, or press 0 to exit...")
    username = input("Enter a username: ")
    if username != "0" and username != "1":
        email = input("Enter email ID: ")
        phone_number = input("Enter phone number: ")
        details = (username, email, phone_number)
        ids = generate_id()
        users_list = {next(ids): i for i in user_details(details)}
        print(users_list)
    elif username == "1":
        for i in range(5):
            print(next(usrs))
    else:
        flag = False
