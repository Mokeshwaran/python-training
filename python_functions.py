def add(a, b, *c):
    d = a + b
    for i in c:
        for j in i:
            d += j
    return d


def exponent(e, b):
    return b ** e


def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * factorial(x - 1)
map(factorial, [1,2,3])

def div(a, b=1):
    return a / b


division = lambda a, b=1: a/b


def mul(a, b, **c):
    d = a * b
    for i, j in c.items():
        for k in j:
            d *= k
    return d


optional = []
flag = True
while flag:
    a = ''
    b = ''
    x = ''
    print("1. Add (A + B + ... + n)\n"
          "2. Exponent (B^A; default B value = 2)\n"
          "3. Factorial (x!)\n"
          "4. Division (A/B)")
    choice = int(input("Enter a choice from above, 0 to exit: "))
    if choice == 0:
        break
    if choice != 3:
        a = input("Value of A: ")
        b = input("Value of B: ")
    else:
        x = input("Value to compute factorial: ")
    match choice:
        case 1:
            while flag:
                values = input("Enter any additional values, or skip pressing 'enter' when empty: ")
                if values == '':
                    break
                optional.append(int(values))
            print(add(int(a), int(b), optional))

        case 2:
            if b == '':
                print(exponent(int(a), b=2))
            else:
                print(exponent(int(a), int(b)))

        case 3:
            print(factorial(int(x)))

        case 4:
            if b == '' or b == '0':
                print("Can't Divide By 0, Dividing By 1...")
                print(division(int(a)))
            else:
                print(division(int(a), int(b)))

        case 5:
            while flag:
                values = input("Enter any additional values, or skip pressing 'enter' when empty: ")
                if values == '':
                    break
                optional.append(int(values))
            print(mul(int(a), int(b), c=optional))
        case _:
            print("Invalid Number")
