import csv


with open("elves.csv") as fin:
    fin.next()
    total = sum(int(r[1]) for r in csv.reader(fin))