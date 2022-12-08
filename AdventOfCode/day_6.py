a = input()
c = list(a)
count = 0
for i in a:
    b = set(c[c.index(i):c.index(i) + 4])
    count += 1
    if len(b) == 4:
        print(count + 3)
        break
    b.clear()
    c.remove(i)


a = input()
c = list(a)
count = 0
for i in a:
    b = set(c[c.index(i):c.index(i) + 14])
    count += 1
    if len(b) == 14:
        print(count + 13)
        break
    b.clear()
    c.remove(i)
