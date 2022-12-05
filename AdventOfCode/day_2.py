# # ROCK(A, X) = 1, PAPER(B, Y) = 2, SCISSOR(C, Z) = 3; WIN = 6, LOSE = 0, DRAW = 3
# score = 0
# flag = True
# while flag:
#     a, s, b = input()
#     if a != 'q' or b != 'q':
#         if a == 'A' and b == 'X':
#             score += 4
#         elif a == 'B' and b == 'Y':
#             score += 5
#         elif a == 'C' and b == 'Z':
#             score += 6
#         elif a == 'A' and b == 'Y':
#             score += 8
#         elif a == 'B' and b == 'Z':
#             score += 9
#         elif a == 'C' and b == 'X':
#             score += 7
#         elif a == 'A' and b == 'Z':
#             score += 3
#         elif a == 'B' and b == 'X':
#             score += 1
#         elif a == 'C' and b == 'Y':
#             score += 2
#     else:
#         flag = False
#
# print(score)

# ROCK(A) = 1, PAPER(B) = 2, SCISSOR(C) = 3; WIN(Z) = 6, LOSE(X) = 0, DRAW(Y) = 3

score = 0
flag = True
while flag:
    a, s, b = input()
    if a != ' ' and b != ' ':
        if a == 'A' and b == 'X':
            score += 3
        elif a == 'B' and b == 'Y':
            score += 5
        elif a == 'C' and b == 'Z':
            score += 7
        elif a == 'A' and b == 'Y':
            score += 4
        elif a == 'B' and b == 'Z':
            score += 9
        elif a == 'C' and b == 'X':
            score += 2
        elif a == 'A' and b == 'Z':
            score += 8
        elif a == 'B' and b == 'X':
            score += 1
        elif a == 'C' and b == 'Y':
            score += 6
    else:
        flag = False

print(score)
