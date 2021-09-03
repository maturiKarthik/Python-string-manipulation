import Arthematic as ar


# The String in python are immutable so converting them in to list is best and easy option
def convert_str_to_list(string):
    return list(string)


# Note: Considering index value
# starting from 0
def make_every_even_index_to_uppercase(string):
    i = 0
    new_string = ""
    list_of_string = convert_str_to_list(string)
    while i < len(list_of_string):
        if ar.check_number_is_even(i):
            new_string += list_of_string[i].upper()
        else:
            new_string += list_of_string[i]
        i += 1
    return new_string


def make_every_prime_index_to_uppercase(string):
    i = 0
    new_string = ""
    list_of_string = convert_str_to_list(string)
    while i < len(string):
        if ar.check_number_is_prime(i):
            new_string += list_of_string[i].upper()
        else:
            new_string += list_of_string[i]
        i += 1
    return new_string
