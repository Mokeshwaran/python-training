import re
# flag = True
# b = []
# count = 0
# while flag:
#     a = input()
#     if a != 'end':
#         a = re.split(',|-', a)
#         index = 0
#         if int(a[0]) >= int(a[2]) and int(a[1]) <= int(a[3]):
#             count += 1
#         elif int(a[0]) <= int(a[2]) and int(a[1]) >= int(a[3]):
#             count += 1
#     else:
#         flag = False
#
# print(count)

flag = True
c = set()
d = set()
count = 0
while flag:
    a = input()
    if a != 'end':
        a = re.split(',|-', a)
        if len(set(range(int(a[0]), int(a[1])+1)) & set(range(int(a[2]), int(a[3])+1))) >= 1:
            count += 1
        # for i in range(int(a[0]), int(a[1])+1):
        #     c.add(i)
        # for j in range(int(a[2]), int(a[3])+1):
        #     d.add(j)
        # print(c & d)
        # if len(c & d) > 0:
        #     count += 1
        # c = set()
        # d = set()
    else:
        flag = False

print(count)

#Optimized Solution
#
# flag = True
# while flag:
#     a = input()
    