from collections import UserDict


class CustomDict(UserDict):
    def pop(self, key):
        try:
            UserDict.pop(self, key)
        except KeyError:
            print("Cannot pop an empty dictionary")


a = {'1': 2, '2': 3, '3': 4}
cd = CustomDict(a)
print(cd.data.get('1'))
flag = True
while flag:
    print(cd)
    b = input("Enter element to pop: ")
    cd.pop(b)
    d = input("Continue: ")
    if d != 'yes':
        break
