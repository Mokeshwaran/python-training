# PROBLEM 1
a = ['[', ']', ']', '[', '{', '}', '(', ')']
b = ['{', '[', '(']
c = ['}', ']', ')']
numbers = {}

for i in a:
    count = 0
    for j in a:
        if i == j:
            count += 1
    numbers[i] = count

count = 0

for j in b:
    if numbers.get(j) is None or numbers.get(c[b.index(j)]) is None:
        print(f"Number of {j}{c[b.index(j)]} is: ", 0)
    elif numbers.get(j) <= numbers.get(c[b.index(j)]):
        count += numbers.get(j)
    else:
        count += numbers.get(c[b.index(j)])

print("Number of open and close pairs is: ", count)


# PROBLEM 2
# a = 'SaVI!872b'
# b = list(a)
# c = ''
# for i in b:
#     if 65 <= ord(i) <= 90:
#         b[a.index(i)] = chr(ord(i) + 32)
#     elif 97 <= ord(i) <= 122:
#         b[a.index(i)] = chr(ord(i) - 32)
#     elif 48 <= ord(i) <= 57:
#         b[a.index(i)] = '0'
#     else:
#         b[a.index(i)] = '#'
#
# for i in b:
#     c += i
#
# print(c)
