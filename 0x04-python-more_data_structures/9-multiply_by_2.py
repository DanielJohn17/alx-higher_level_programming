#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    nw_list = list(new_dict.keys())

    for i in nw_list:
        new_dict[i] *= 2
        print(new_dict[i])
    return new_dict



