#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
string = "Last digit of"
ls_num = number % 10
if ls_num > 5:
    print(f"{string} {number} is {ls_num} and greater than 5")
elif ls_num < 6 and ls_num != 0:
    print(f"{string} {number} is {ls_num} and less than 6 and not 0")
else:
    print(f"{string} {number} is {ls_num} and is 0")
