a = ['V', 'C', 'W', 'L', 'R', 'M', 'F', 'Q']
b = ['L', 'Q', 'D']
c = ['B', 'N', 'C', 'W', 'G', 'R', 'S', 'P']
d = ['G', 'Q', 'B', 'H', 'D', 'C', 'L']
e = ['S', 'Z', 'F', 'L', 'G', 'V']
f = ['P', 'N', 'G', 'D']
g = ['W', 'C', 'F', 'V', 'P', 'Z', 'D']
h = ['S', 'M', 'D', 'P', 'C']
j = ['C', 'P', 'M', 'V', 'T', 'W', 'N', 'Z']
di = {'1': a, '2': b, '3': c, '4': d, '5': e, '6': f, '7': g, '8': h, '9': j}
flag = True
while flag:
    user_input = input()
    if user_input != 'end':
        user_input = user_input.split(' ')
        for i in range(int(user_input[1])):
            di[user_input[5]].insert(0, di[user_input[3]][0])
            di[user_input[3]].pop(0)
    else:
        flag = False

print(a[0], b[0], c[0], d[0], e[0], f[0], g[0], h[0], j[0])
#
# a = ['V', 'C', 'W', 'L', 'R', 'M', 'F', 'Q']
# b = ['L', 'Q', 'D']
# c = ['B', 'N', 'C', 'W', 'G', 'R', 'S', 'P']
# d = ['G', 'Q', 'B', 'H', 'D', 'C', 'L']
# e = ['S', 'Z', 'F', 'L', 'G', 'V']
# f = ['P', 'N', 'G', 'D']
# g = ['W', 'C', 'F', 'V', 'P', 'Z', 'D']
# h = ['S', 'M', 'D', 'P', 'C']
# k = ['C', 'P', 'M', 'V', 'T', 'W', 'N', 'Z']
# di = {'1': a, '2': b, '3': c, '4': d, '5': e, '6': f, '7': g, '8': h, '9': k}
# flag = True
# while flag:
#     user_input = input()
#     if user_input != 'end':
#         user_input = user_input.split(' ')
#         for j in range(int(user_input[1])):
#             di[user_input[5]].insert(j, di[user_input[3]][j])
#         for i in range(int(user_input[1])):
#             di[user_input[3]].pop(0)
#     else:
#         flag = False
#
#
# print(a[0], b[0], c[0], d[0], e[0], f[0], g[0], h[0], k[0])
