users = [(1, "John", 15), (2, "Mike", 17), (3, "Joe", 19)]
details = ("id", "name", "age")
dict_list = []

for i in users:
    user_dict = {}
    for j in range(len(details)):
        user_dict[details[j]] = i[j]
    dict_list.append(user_dict)

print(dict_list)
