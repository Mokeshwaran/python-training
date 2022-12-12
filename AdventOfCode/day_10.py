# cycles = 0
# x = 1
# temp = 0
# freq_1 = [20, 60, 100, 140, 180, 220]
# freq = {}
# flag = True
# while flag:
#     a = input()
#     if 'end' in a:
#         break
#     if 'noop' in a:
#         cycles += 1
#     if 'addx' in a:
#         a = a.split(' ')
#         for i in range(2):
#             cycles += 1
#             x += temp
#             temp = 0
#             if cycles in freq_1:
#                 temp = int(a[1])
#                 break
#             elif i == 1:
#                 x += int(a[1])
#     if cycles in freq_1:
#         freq[freq_1[freq_1.index(cycles)]] = cycles * x
#
# print(sum(freq.values()))


cycles = 0
x = 1
temp = 0
freq_1 = [20, 60, 100, 140, 180, 220]
freq_2 = [40, 80, 120, 160, 200, 240]
freq = {}
flag = True
row = 0
crt = [['.']*40 for i in range(6)]
print(crt)
while flag:
    a = input()
    # col = cycles % 40
    # sprite_location = [x - 1, x, x + 1]
    # print("Cycle:", cycles)
    # if cycles in freq_2 and row < 5:
    #     row += 1
    # if col in sprite_location:
    #     print(row, col)
    #     crt[row][col] = '#'
    if 'end' in a:
        break
    if 'noop' in a:
        col = cycles % 40
        sprite_location = [x - 1, x, x + 1]
        print("Cycle:", cycles)
        if cycles in freq_2 and row < 5:
            row += 1
        if col in sprite_location:
            print(row, col)
            print(x, sprite_location)
            # if x in sprite_location:
            crt[row][col] = '#'
        cycles += 1
    if 'addx' in a:
        a = a.split(' ')
        for i in range(2):
            col = cycles % 40
            sprite_location = [x - 1, x, x + 1]
            print("Cycle:", cycles)
            if cycles in freq_2 and row < 5:
                row += 1
            if col in sprite_location:
                print(row, col)
                print(x, sprite_location)
                # if x in sprite_location:
                crt[row][col] = '#'
            cycles += 1
            x += temp
            temp = 0
            if cycles in freq_1:
                temp = int(a[1])
                break
            elif i == 1:
                x += int(a[1])
    if cycles in freq_1:
        freq[freq_1[freq_1.index(cycles)]] = cycles * x

for i in crt:
    print(i)
print(sum(freq.values()))







# while flag:
#     a = input()
#     if 'end' in a:
#         break
#     if 'noop' in a:
#         cycles += 1
#     if 'addx' in a:
#         a = a.split(' ')
#         for i in range(2):
#             cycles += 1
#             x += temp
#             temp = 0
#             if cycles in freq_1:
#                 temp = int(a[1])
#                 break
#             elif i == 1:
#                 x += int(a[1])
#     if cycles in freq_1:
#         freq[freq_1[freq_1.index(cycles)]] = cycles * x
#     if cycles in freq_2:
#         print('Cycles: ', cycles)
#         row += 1
#     sprite_location = [x - 1, x, x + 1]
#     col = cycles % 40
#     print(col, sprite_location)
#     if cycles in freq_2:
#         row += 1
#     if cycles in sprite_location:
#         print(row, col)
#         crt[row][col] = '#'