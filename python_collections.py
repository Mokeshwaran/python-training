import os
from collections import Counter


path = os.getcwd()
with open(path + "\\names.txt", 'r') as names:
    name = names.readlines()
    person_name = Counter(name)

print(person_name.items())

