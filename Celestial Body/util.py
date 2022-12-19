import re


def is_valid_name(name):
    is_valid = re.match("[A-Za-z](-[0-9][a-z])?", name)
    return is_valid


def is_valid_number(number):
    is_valid = re.match("\\d", number)
    return is_valid


def is_valid_cluster_name(name):
    is_valid = re.match("[A-Za-z]", name)
    return is_valid
