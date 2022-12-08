# flag = True
# lst = []
# while flag:
#     a = input()
#     lst_2 = []
#     if a == 'end':
#         break
#     for i in a:
#         lst_2.append(i)
#     lst.append(lst_2)
#     print(lst)
#
# n = 1
# m = 0
# total = 0
# for i in range(1, len(lst) - 1):
#     right = 'visible'
#     left = 'visible'
#     for j in range(1, len(lst) - 1):
#         right = 'visible'
#         left = 'visible'
#         top = 'visible'
#         bottom = 'visible'
#         if m == (len(lst) - 2):
#             m = 0
#         for k in range(len(lst)):
#             if j <= k:
#                 continue
#             elif lst[i][j] <= lst[i][k]:
#                 # print("Left loop:", lst[i][k], lst[i][j])
#                 left = ''
#         for l in range(len(lst)):
#             if j >= l:
#                 continue
#             elif lst[i][j] <= lst[i][l]:
#                 # print("Right loop:", lst[i][l], lst[i][j])
#                 right = ''
#         for v in range(len(lst)):
#             if i >= v:
#                 continue
#             elif lst[i][j] <= lst[v][j]:
#                 # print("Bottom loop:", lst[v][j], lst[i][j], v, j)
#                 bottom = ''
#         for o in range(len(lst)):
#             if i <= o:
#                 continue
#             elif lst[i][j] <= lst[o][j]:
#                 # print("Top loop:", lst[o][j], lst[i][j], o, j)
#                 top = ''
#         if j - 1 == j:
#             continue
#         else:
#             # print("Prev:", lst[i][m], "Next:", lst[i][j + 1])
#             ...
#         # print("Left:", left, "Right:", right, "Top:", top, "Bottom:", bottom, "\n")
#         if top == 'visible' or bottom == 'visible' or left == 'visible' or right == 'visible':
#             total += 1
#             print(total)
#         m += 1
#     # n += 1
#
# print(total + ((len(lst) - 1) * 4))


flag = True
lst = []
while flag:
    a = input()
    lst_2 = []
    if a == 'end':
        break
    for i in a:
        lst_2.append(i)
    lst.append(lst_2)
    print(lst)

n = 1
m = 0
total = 0
max = 0
for i in range(1, len(lst) - 1):
    right = 'visible'
    left = 'visible'
    for j in range(1, len(lst) - 1):
        right = 0
        left = 0
        top = 0
        bottom = 0
        if m == (len(lst) - 2):
            m = 0
        for k in range(j-1, -1, -1):
            if j == k:
                continue
            if lst[i][j] <= lst[i][k]:
                print("Left loop 1:", lst[i][k], lst[i][j])
                left += 1
                break
            elif lst[i][j] > lst[i][k]:
                print("Left loop 2:", lst[i][k], lst[i][j])
                left += 1
        # print(left)
        for l in range(j, len(lst)):
            if j == l:
                continue
            if lst[i][j] <= lst[i][l]:
                print("Right loop 1:", lst[i][l], lst[i][j])
                right += 1
                break
            elif lst[i][j] > lst[i][l]:
                print("Right loop 2:", lst[i][l], lst[i][j])
                right += 1
        # print(right)
        for v in range(i-1, -1, -1):
            print(v, j)
            if i == v:
                continue
            if lst[i][j] <= lst[v][j]:
                print("top loop 1:", lst[v][j], lst[i][j], v, j)
                top += 1
                break
            elif lst[i][j] > lst[v][j]:
                print("top loop 2:", lst[v][j], lst[i][j], v, j)
                top += 1
        # print(bottom)
        for o in range(i, len(lst)):
            if i == o:
                continue
            if lst[i][j] <= lst[o][j]:
                print("bottom loop 1:", lst[o][j], lst[i][j], o, j)
                bottom += 1
                break
            elif lst[i][j] > lst[o][j]:
                print("bottom loop 2:", lst[o][j], lst[i][j], o, j)
                bottom += 1
        # print(top)
        if j - 1 == j:
            continue
        else:
            # print("Prev:", lst[i][m], "Next:", lst[i][j + 1])
            ...
        print("Left:", left, "Right:", right, "Top:", top, "Bottom:", bottom, "\n")
        total = top * bottom * right * left
        if total > max:
            max = total
            print("Total: ", total)
        m += 1
    # n += 1

print("Max: ", max)

# 3x3 = 8 = 4x2
# 4x4 = 12 = 4x3
# 5x5 = 16 = 4x4
# 6x6 = 20 = 4x5
#
# for i in lst:
#     print(lst[len(lst) - n][1])
#     n -= 1
# n = len(lst)
# for j in lst:
#     print(lst[1][len(lst) - n], end='')
#     n -= 1
