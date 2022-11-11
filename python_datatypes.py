Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
dir(tuple)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
help(list.__add__)
Help on wrapper_descriptor:

__add__(self, value, /)
    Return self+value.

help(list.append)
Help on method_descriptor:

append(self, object, /)
    Append object to the end of the list.

help(set.difference_update)
Help on method_descriptor:

difference_update(...)
    Remove all elements of another set from this set.

help(set.isdisjoint)
Help on method_descriptor:

isdisjoint(...)
    Return True if two sets have a null intersection.

help(set.discard)
Help on method_descriptor:

discard(...)
    Remove an element from a set if it is a member.
    
    If the element is not a member, do nothing.

help(set.update)
Help on method_descriptor:

update(...)
    Update a set with the union of itself and others.

help(set.intersection_update)
Help on method_descriptor:

intersection_update(...)
    Update a set with the intersection of itself and another.

help(set.symmetric_difference_update)
Help on method_descriptor:

symmetric_difference_update(...)
    Update a set with the symmetric difference of itself and another.

help(list.__delitem__)
Help on wrapper_descriptor:

__delitem__(self, key, /)
    Delete self[key].

help(list.__format__)
Help on method_descriptor:

__format__(self, format_spec, /)
    Default object formatter.

help(list.__ge__)
Help on wrapper_descriptor:

__ge__(self, value, /)
    Return self>=value.

help(list.__gt__)
Help on wrapper_descriptor:

__gt__(self, value, /)
    Return self>value.

help(list.__ne__)
Help on wrapper_descriptor:

__ne__(self, value, /)
    Return self!=value.

help(list.__iadd__)
Help on wrapper_descriptor:

__iadd__(self, value, /)
    Implement self+=value.

help(list.__iter__)
Help on wrapper_descriptor:

__iter__(self, /)
    Implement iter(self).

help(list.__dir__)
Help on method_descriptor:

__dir__(self, /)
    Default dir() implementation.

help(list.__doc__)
No Python documentation found for 'Built-in mutable sequence.\n\nIf no argument is given, the constructor creates a new empty list.\nThe argument must be an iterable if specified.'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

help(list.__getattribute__)
Help on wrapper_descriptor:

__getattribute__(self, name, /)
    Return getattr(self, name).

KeyboardInterrupt
help(list.__repr__)
Help on wrapper_descriptor:

__repr__(self, /)
    Return repr(self).

help(list.__class__)
Help on class type in module builtins:

class type(object)
 |  type(object) -> the object's type
 |  type(name, bases, dict, **kwds) -> a new type
 |  
 |  Methods defined here:
 |  
 |  __call__(self, /, *args, **kwargs)
 |      Call self as a function.
 |  
 |  __delattr__(self, name, /)
 |      Implement delattr(self, name).
 |  
 |  __dir__(self, /)
 |      Specialized __dir__ implementation for types.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __instancecheck__(self, instance, /)
 |      Check if an object is an instance.
 |  
 |  __or__(self, value, /)
 |      Return self|value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __ror__(self, value, /)
 |      Return value|self.
 |  
 |  __setattr__(self, name, value, /)
 |      Implement setattr(self, name, value).
 |  
 |  __sizeof__(self, /)
 |      Return memory consumption of the type object.
 |  
 |  __subclasscheck__(self, subclass, /)
 |      Check if a class is a subclass.
 |  
 |  __subclasses__(self, /)
 |      Return a list of immediate subclasses.
 |  
 |  mro(self, /)
 |      Return a type's method resolution order.
 |  
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |  
 |  __prepare__(...)
 |      __prepare__() -> dict
 |      used to create the namespace for the class statement
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs)
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __abstractmethods__
 |  
 |  __annotations__
 |  
 |  __dict__
 |  
 |  __text_signature__
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __base__ = <class 'object'>
 |      The base class of the class hierarchy.
 |      
 |      When called, it accepts no arguments and returns a new featureless
 |      instance that has no instance attributes and cannot be given any.
 |  
 |  
 |  __bases__ = (<class 'object'>,)
 |  
 |  __basicsize__ = 888
 |  
 |  __dictoffset__ = 264
 |  
 |  __flags__ = 2148031744
 |  
 |  __itemsize__ = 40
 |  
 |  __mro__ = (<class 'type'>, <class 'object'>)
 |  
 |  __weakrefoffset__ = 368

help(list.__class_iterm__)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    help(list.__class_iterm__)
AttributeError: type object 'list' has no attribute '__class_iterm__'. Did you mean: '__class_getitem__'?
help(list.__class_getitem__)
Help on built-in function __class_getitem__:

__class_getitem__(...) method of builtins.type instance
    See PEP 585

help(list.__delattr__)
Help on wrapper_descriptor:

__delattr__(self, name, /)
    Implement delattr(self, name).

6 __lt__ 5
SyntaxError: invalid syntax
a = [1,2,3,4,5]
b = [6,7,8,9,10]
a __lt__ b
SyntaxError: invalid syntax
a__lt__b
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a__lt__b
NameError: name 'a__lt__b' is not defined
a.__lt__(b)
True
b.__lt__(a)
False
a = [1,9,2,8,3]
b = [7,4,6,5,0]
a.__lt__(b)
True
b.__lt__(a)
False
help(list.__rmul__)
Help on wrapper_descriptor:

__rmul__(self, value, /)
    Return value*self.

a.__rmul__(10)
[1, 9, 2, 8, 3, 1, 9, 2, 8, 3, 1, 9, 2, 8, 3, 1, 9, 2, 8, 3, 1, 9, 2, 8, 3, 1, 9, 2, 8, 3, 1, 9, 2, 8, 3, 1, 9, 2, 8, 3, 1, 9, 2, 8, 3, 1, 9, 2, 8, 3]
a.__rmul__(3)
[1, 9, 2, 8, 3, 1, 9, 2, 8, 3, 1, 9, 2, 8, 3]
help(list.__reduce_ex__)
Help on method_descriptor:

__reduce_ex__(self, protocol, /)
    Helper for pickle.

help(list.__subclasshook__)
Help on built-in function __subclasshook__:

__subclasshook__(...) method of builtins.type instance
    Abstract classes can override this to customize issubclass().
    
    This is invoked early on by abc.ABCMeta.__subclasscheck__().
    It should return True, False or NotImplemented.  If it returns
    NotImplemented, the normal algorithm is used.  Otherwise, it
    overrides the normal algorithm (and the outcome is cached).

a.__subclasshook__(b)
NotImplemented
help(list.__iadd__)
Help on wrapper_descriptor:

__iadd__(self, value, /)
    Implement self+=value.

a.__iadd__(3)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a.__iadd__(3)
TypeError: 'int' object is not iterable
a.__iadd__(b)
[1, 9, 2, 8, 3, 7, 4, 6, 5, 0]
a
[1, 9, 2, 8, 3, 7, 4, 6, 5, 0]
a.add(b)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a.add(b)
AttributeError: 'list' object has no attribute 'add'
a.__add__(b)
[1, 9, 2, 8, 3, 7, 4, 6, 5, 0, 7, 4, 6, 5, 0]
a
[1, 9, 2, 8, 3, 7, 4, 6, 5, 0]
help(list.__hash__)
Help on NoneType object:

class NoneType(object)
 |  Methods defined here:
 |  
 |  __bool__(self, /)
 |      True if self else False
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

help(set.__ior__)
Help on wrapper_descriptor:

__ior__(self, value, /)
    Return self|=value.

help(list.__ior__)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    help(list.__ior__)
AttributeError: type object 'list' has no attribute '__ior__'. Did you mean: '__dir__'?
help(list.__or__)
Help on method-wrapper:

__or__ = <method-wrapper '__or__' of type object>
    Return self|value.

\
help(set.__ror__)
Help on wrapper_descriptor:

__ror__(self, value, /)
    Return value|self.

a = {a,b,c}
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a = {a,b,c}
NameError: name 'c' is not defined
a = {1,2,3}
b = {2}
b = {2,3,4}
a.__or__(b)
{1, 2, 3, 4}
a.__ior__(b)
{1, 2, 3, 4}
a.__ror__(b)
{1, 2, 3, 4}
a = {1,2,3}
b = {1,2,3}
a.__or__(b)
{1, 2, 3}
a.__ior__(b)
{1, 2, 3}
a.__ror__(b)
{1, 2, 3}
a.__rxor__(b)
set()
a = {1,2,3,4,5,6,7,8}
b = {1,0,2,9,8,7,6}
a.__rxor__(b)
{0, 3, 4, 5, 9}
b.__rxor__(a)
{0, 3, 4, 5, 9}
a.__xor__(b)
{0, 3, 4, 5, 9}
b.__xor__(a)
{0, 3, 4, 5, 9}
b.__ixor__(a)
{0, 3, 4, 5, 9}
a.__ixor__(b)
{0, 1, 2, 6, 7, 8, 9}
\
a.__ixor__(b)
{1, 2, 4, 3, 6, 7, 8, 5}
a.__ixor(b)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a.__ixor(b)
AttributeError: 'set' object has no attribute '__ixor'. Did you mean: '__ixor__'?
a.__ixor__(b)
{1, 2, 6, 7, 8, 0, 9}
a.__ixor__(b)
{1, 2, 4, 6, 7, 8, 3, 5}
a.__ixor__(b)
{1, 2, 6, 7, 8, 0, 9}
a.__ixor__(b)
{1, 2, 5, 6, 7, 8, 4, 3}
a.__ixor__(b)
{1, 2, 6, 7, 8, 9, 0}
a.__ixor__(b)
{1, 2, 5, 6, 7, 8, 4, 3}
a.__ixor__(b)
{1, 2, 6, 7, 8, 0, 9}
a.__ixor__(b)
{1, 2, 5, 6, 7, 8, 4, 3}
a.__ixor__(b)
{1, 2, 6, 7, 8, 9, 0}
a
{1, 2, 6, 7, 8, 9, 0}
a.__ixor__(b)
{1, 2, 5, 6, 7, 8, 4, 3}
a
{1, 2, 5, 6, 7, 8, 4, 3}
b
{0, 3, 4, 5, 9}
a.__ixor__(b)
{1, 2, 6, 7, 8, 0, 9}
b
{0, 3, 4, 5, 9}
a.__rxor__(b)
{1, 2, 3, 4, 5, 6, 7, 8}
a
{1, 2, 6, 7, 8, 0, 9}
a.__rxor__(b)
{1, 2, 3, 4, 5, 6, 7, 8}
b
{0, 3, 4, 5, 9}
a.__rxor__(b)
{1, 2, 3, 4, 5, 6, 7, 8}
b
{0, 3, 4, 5, 9}
a.__rxor__(b)
{1, 2, 3, 4, 5, 6, 7, 8}
b
{0, 3, 4, 5, 9}
a.__xor__(b)
{1, 2, 3, 4, 5, 6, 7, 8}
a
{1, 2, 6, 7, 8, 0, 9}
a.__rxor__(b)
{1, 2, 3, 4, 5, 6, 7, 8}
b
{0, 3, 4, 5, 9}
a
{1, 2, 6, 7, 8, 0, 9}
a.__rxor__(b)
{1, 2, 3, 4, 5, 6, 7, 8}
b
{0, 3, 4, 5, 9}
a
{1, 2, 6, 7, 8, 0, 9}
a.__xor__(b)
{1, 2, 3, 4, 5, 6, 7, 8}
a
{1, 2, 6, 7, 8, 0, 9}
b
{0, 3, 4, 5, 9}
a = {1,2,3,4,5,6}
b = {0,9,8,7,6,5}
a.__xor__(b)
{0, 1, 2, 3, 4, 7, 8, 9}
a
{1, 2, 3, 4, 5, 6}
b
{0, 5, 6, 7, 8, 9}
b.__xor__(b)
set()
b.__xor__(a)
{0, 1, 2, 3, 4, 7, 8, 9}
a
{1, 2, 3, 4, 5, 6}
b
{0, 5, 6, 7, 8, 9}
a.__rxor__(b)
{0, 1, 2, 3, 4, 7, 8, 9}
a
{1, 2, 3, 4, 5, 6}
b
{0, 5, 6, 7, 8, 9}
help(set.__rsub__)
Help on wrapper_descriptor:

__rsub__(self, value, /)
    Return value-self.

help(dict.update)
Help on method_descriptor:

update(...)
    D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
    If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
    In either case, this is followed by: for k in F:  D[k] = F[k]

help(dict.pop)
Help on method_descriptor:

pop(...)
    D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
    
    If the key is not found, return the default if given; otherwise,
    raise a KeyError.

help(dict.popitem)
Help on method_descriptor:

popitem(self, /)
    Remove and return a (key, value) pair as a 2-tuple.
    
    Pairs are returned in LIFO (last-in, first-out) order.
    Raises KeyError if the dict is empty.

help(dict.setdefault)
Help on method_descriptor:

setdefault(self, key, default=None, /)
    Insert key with a value of default if key is not in the dictionary.
    
    Return the value for key if key is in the dictionary, else default.

help(dict.items)
Help on method_descriptor:

items(...)
    D.items() -> a set-like object providing a view on D's items

