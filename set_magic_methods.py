def and_operation(primary, secondary):
    print(primary.__and__(secondary))
    print(primary.__iand__(secondary))
    print(primary.__rand__(secondary))


def xor_operation(primary, secondary):
    print(primary.__xor__(secondary))
    print(primary.__ixor__(secondary))
    print(primary.__rxor__(secondary))


def or_operation(primary, secondary):
    print(primary.__or__(secondary))
    print(primary.__ior__(secondary))
    print(primary.__ror__(secondary))


def sub_operation(primary, secondary):
    print(primary.__sub__(secondary))
    print(primary.__isub__(secondary))
    print(primary.__rsub__(secondary))


def not_equal(primary, secondary):
    print(primary.__ne__(secondary))


def equal(primary, secondary):
    print(primary.__eq__(secondary))


def greater_than_equal(primary, secondary):
    print(primary.__ge__(secondary))


def lesser_than_equal(primary, secondary):
    print(primary.__le__(secondary))


def greater_than(primary, secondary):
    print(primary.__gt__(secondary))


def lesser_than(primary, secondary):
    print(primary.__lt__(secondary))


def length_operation(primary):
    print(primary.__len__())


def repr_operation(primary):
    print(primary.__repr__())


def str_operation(primary):
    print(primary.__str__())


def sizeof_set(primary):
    print(primary.__sizeof__())


def contains_element(primary):
    print(primary.__contains__('4'))


primary = {'1', '2', '3', '4', '5'}
secondary = {'4', '5', '6', '7', '8'}
or_operation(primary, secondary)

primary = {'1', '2', '3', '4', '5'}
secondary = {'4', '5', '6', '7', '8'}
and_operation(primary, secondary)

primary = {'1', '2', '3', '4', '5'}
secondary = {'4', '5', '6', '7', '8'}
xor_operation(primary, secondary)

primary = {'1', '2', '3', '4', '5'}
secondary = {'4', '5', '6', '7', '8'}
sub_operation(primary, secondary)

primary = {'1', '2', '3', '4', '5'}
secondary = {'1', '2', '3'}
not_equal(primary, secondary)

primary = {'1', '2', '3', '4', '5'}
secondary = {'1', '2', '3'}
equal(primary, secondary)

primary = {'1', '2', '3', '4', '5'}
secondary = {'1', '2', '3'}
lesser_than(primary, secondary)

primary = {'1', '2', '3', '4', '5'}
secondary = {'1', '2', '3'}
lesser_than_equal(primary, secondary)

primary = {'1', '2', '3', '4', '5'}
secondary = {'1', '2', '3'}
greater_than(primary, secondary)

primary = {'1', '2', '3', '4', '5'}
secondary = {'1', '2', '3'}
greater_than_equal(primary, secondary)

primary = {'1', '2', '3', '4', '5'}
length_operation(primary)
sizeof_set(primary)
repr_operation(primary)
str_operation(primary)
contains_element(primary)