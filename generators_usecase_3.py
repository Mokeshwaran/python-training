import csv

file_name = "./trees.csv"


def tree_details():
    with open(file_name, 'r') as trees:
        read = csv.reader(trees)
        for row in read:
            yield row


flag = True
tree = tree_details()
while flag:
    choice = input("Press enter to view next 5 tree's measurements, 0 to exit: ")
    if choice != "0":
        for i in range(5):
            print(next(tree))
    else:
        flag = False
