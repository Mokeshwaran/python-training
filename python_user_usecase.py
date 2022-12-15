from collections import UserString, UserList, UserDict
from typing import Self, Any, Optional, List


class CustomString(UserString):
    def center(self: Optional[Self] = 'self', width: Optional[int] = 0, char: Optional[str] = '') -> Self:
        return f"{char * width}{self}"

    def title(self: Self) -> Self:
        return self.lower()


class CustomList(UserList):
    def append(self, item: Any) -> Any:
        return self.pop(item)

    def pop(self, i: Any = ...) -> Self:
        UserList.append(self, i)
        return self


class CustomDict(UserDict):
    def copy(self):
        return self.__len__()


a_string = "Some String"
b_dict = {'a': 1, 'b': 2, 'c': 3}
custom_string = CustomString(a_string)
custom_list = CustomList()
custom_dict = CustomDict(b_dict)

print(custom_string.center(5, '!!!'))
print(custom_string.title())

print(custom_list.pop(a_string))
print(custom_list.append('S'))

print(custom_dict.copy())
