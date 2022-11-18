def user_details(username, details):
    user_detail = (username, details)
    users.append(user_detail)
    return users


users = []
flag = True
while flag:
    print("Enter username, or press 0 to exit...")
    username = input("Enter a username: ")
    if username != "0":
        email = input("Enter email ID: ")
        phone_number = input("Enter phone number: ")
        details = (email, phone_number)
        users_list = {i[0]: j for i in user_details(username, details) for j in i}
        print(users_list)
    else:
        flag = False
