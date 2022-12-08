# $ cd /
# $ ls
# dir a
# 14848 b.txt
# 8504 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 40601 j
# 80330 d.log
# 5626 d.ext
# 72142 k
import itertools


# flag = True
# c = []
# n = 0
# m = 0
# total = 0
# dicti = {}
# while flag:
#     a = input()
#     if a != 'end' and '$ cd /' in a:
#         n += 1
#         print('\n$ cd /: ')
#         while flag:
#             b = input()
#             if 'dir' in b:
#                 continue
#             elif '$ ls' in b:
#                 continue
#             if '$ cd ..' not in b and '$ cd' in b or b[0].isdigit():
#                 print('\t' * n, b + ':')
#                 n += 1
#                 if not b[0].isdigit():
#                     dicti[b] = 0
#                 if b[0].isdigit() and 'dir' not in b:
#                     d = b.split(' ')
#                     if n <= 1 and int(d[0]) <= 100000:
#                         print('\t' * n, int(d[0]))
#                         total += int(d[0])
#                         dicti[m] = total
#                         m += 1
#                     elif n > 1 and int(d[0]) <= 100000:
#                         print('\t' * n, int(d[0]))
#                         total += (int(d[0]) * (n - 1))
#                         dicti[m] = total
#                         m += 1
#                     else:
#                         print('\t' * n, "More than 100000")
#
#             elif "$ cd .." in b:
#                 print('\t' * n, '----')
#                 n -= 1
#             else:
#                 break
#     else:
#         flag = False
#
# print("Total: ", total)
# print(dicti)

# def rec(flag, n):
#     while flag:
#         a = input()
#         if '$ cd ' in a and '$ cd ..' not in a and a != 'end':
#             print(a)
#             n += 1
#             if d.get(a) is None:
#                 d[a] = 0
#                 print("LLLL", d)
#             else:
#                 d[a + str(n)] = 0
#                 print("MMMM", d)
#             while flag:
#                 b = input()
#                 if b[0].isdigit():
#                     b = b.split()
#                     print("B[0]: ", b[0])
#                     if int(b[0]) <= 100000:
#                         d[a] += int(b[0])
#                         print("OOOO", d)
#                 elif 'dir' in b or '$ cd ..' in b:
#                     continue
#                 elif '$ cd' in b and '$ ls' not in b:
#                     rec(flag, n)
#                 elif b == 'end':
#                     flag = False
#             flag = True
#         elif '$ ls' in a or 'dir' in a or '$ cd ..' in a:
#             continue
#         elif a == 'end':
#             flag = False
#
#
# d = {}
# flag = True
# n = 0
# rec(flag, n)
# xyz = d.values()
# print(sum(xyz))

# def rec(a, b, c, n, e):
#     print("REC :", a)
#     print("SUM :", sum(e))
#     print("DICT :", c)
#     if '$ cd' in a and '$ cd ..' not in a:
#         b.append(a)
#         c[a] = 0
#         n += 1
#         print("List B: ", b)
#         return b
#     if a[0].isdigit():
#         d = a.split(' ')
#         print("isDigit :", d)
#         if 100000 >= int(d[0]) > 1:
#             e.append(int(d[0]))
#             c[b[n]] = e
#         return c
#     elif '$ ls' in a or 'dir' in a or '$ cd ..' in a:
#         return c
#     return rec(a, b, c, n, e)
#
#
# n = -1
# e = []
# b = []
# c = {}
# flag = True
# while flag:
#     a = input()
#     if a == 'end':
#         break
#     print(rec(a, b, c, n, e))

# AFTER NUMEROUS FAILURE ATTEMPTS I DECIDED TO GIVE UP CUZ I AM NOT THAT BRILLIANT.
# STOLEN FROM THE HUB

# from collections import defaultdict
# from itertools import accumulate
# from operator import concat
#
# total_space = 70000000
# required_space = 30000000
# max_size = 100000
# curr_dir_path = list()
# dir_tree = defaultdict(lambda: 0)
#
#
# def keep_useful_info(entry):
#     # keep only directory changes and file size
#     return (True, entry[1]) if entry[0] == "$ cd" else (False, int(entry[0])) if entry[0][0].isdigit() else None
#
#
# with open('input.txt', 'r') as file:
#     commands = filter(bool, map(keep_useful_info, (line.strip('\n').rsplit(' ', 1) for line in file)))
#     while True:
#         try:
#             change_dir, info = next(commands)
#             if change_dir:
#                 curr_dir_path.pop() if info == ".." else curr_dir_path.append(info)
#             else:
#                 for directory in accumulate(curr_dir_path, concat):  # the name of a directory is its path
#                     dir_tree[directory] += info
#         except StopIteration:
#             break
#
# # PART ONE
# print(sum(filter(lambda x: x <= max_size, dir_tree.values())))
#
# # PART TWO
# to_del_space = required_space - (total_space - dir_tree["/"])  # required space - free space
# print(to_del_space + min(filter(lambda x: x >= 0, map(lambda dir_size: dir_size - to_del_space, dir_tree.values()))))

# lst_1 = []
# lst_2 = []
#
# def day_7(a):
#     if '$ cd' in a:
#         lst_1.append(a)
#         return lst_1
#     if 'dir' in a or a[0].isdigit():
#         lst_2.append(a)
#         return lst_2
#     if '$ ls' in a:
#         return 0
#
#
# flag = True
# while flag:
#     a = input()
#     if a == 'end':
#         break
#     day_7(a)
# print(lst_1, lst_2)

dir_dict = {}
ls_count = -1
total = 0
flag = True
while flag:
    user_input = input()
    if '$ cd' in user_input and '$ cd ..' not in user_input:
        if dir_dict.get(user_input) is None:
            dir_dict[user_input] = 0
        else:
            dir_dict[user_input + str(ls_count)] = 0
        total = 0
    if '$ ls' in user_input:
        ls_count += 1
    if user_input[0].isdigit():
        user_input = user_input.split(' ')
        if int(user_input[0]) <= 100000:
            total += int(user_input[0])
        dir_dict[list(dir_dict.keys())[ls_count]] = total
    if user_input == 'end':
        flag = False
print(dir_dict)
print(sum(dir_dict.values()))