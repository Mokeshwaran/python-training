from collections import UserString


class CustomString(UserString):
    def isdigit(self):
        return UserString.title(self)


a = "saline treatment plant"
cs = CustomString(a)

print(cs.isdigit())
