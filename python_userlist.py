from collections import UserList


class CustomList(UserList):
    def append(self, item):
        print("Cannot append in List like Tuple")

    def pop(self, i: str = ...):
        UserList.append(self, i)


a = ['a', 'b', 'c', 'd']
cl = CustomList(a)
cl.append('n')
cl.pop('l')
print(cl)
