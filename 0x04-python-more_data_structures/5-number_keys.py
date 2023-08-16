#!/usr/bin/python3
def number_keys(a_dictionary):
    keys_list = list(a_dictionary.keys())
    num = 0

    for i in range(len(keys_list)):
        num += i
    return num
