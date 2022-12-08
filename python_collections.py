import os
from collections import Counter, OrderedDict


path = os.getcwd()
with open(path + "\\names.txt", 'r') as names:
    name = names.readlines()
    person_name = Counter(name)

print(person_name.keys())

od = OrderedDict()
d = {'a': 1, 'b': 2, 'c': 3}
d['b'] = 5
print(d)