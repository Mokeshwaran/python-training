age = [1, 23, 43, 11, 32, 87, 21, 19, 18, 4, 27]
print([x if x >= 18 else "Under 18" for x in age])
# The above comprehension works like,
# a = []
# for x in age:
#     if x >= 18:
#         a.append(x)
#     else:
#         a.append("Under 18")
# print(a)
