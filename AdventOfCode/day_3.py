# priority = 0
# flag = True
# while flag:
#     a = input()
#     length = int(len(a) / 2)
#     b, c = a[:length], a[length:]
#     if a != 'end':
#         for i in b:
#             for j in c:
#                 if i == j:
#                     if i.islower():
#                         priority += ord(i) - 96
#                         break
#                     elif i.isupper():
#                         priority += ord(i) - 38
#                         break
#     else:
#         flag = False
#
#
# print(priority)

b = []
priority = 0
flag = True
while flag:
    a = input()
    b.append(a)
    if a != "end":
        if len(b) == 3:
            c = list(set(b[0]) & set(b[1]) & set(b[2]))
            b = []
            if c[0].islower():
                priority += ord(c[0]) - 96
            elif c[0].isupper():
                priority += ord(c[0]) - 38
    else:
        flag = False

print(priority)

