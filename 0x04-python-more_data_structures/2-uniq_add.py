#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set(my_list)
    num = 0

    for i in uniq_set:
        num += i

    return num


my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))
