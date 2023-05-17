import re
import numpy as np

def init():
    print("Init...")


def sum_two_smallest_numbers(numbers):
    theSum = 0
    theNumbers = sorted(numbers)[:2]
    for i in range(2):
        theSum += sorted(numbers)[:2][i]

    return theSum


def find_short(s):
    l = 1000
    arr = str(s).split()

    for idx, y in enumerate(arr):
        if l > len(y) : l = len(y)

    return l

def find_short_snygg(s):
    return len(sorted(s.split(), key=len)[0])

if __name__ == '__main__':
    init()
    # print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
    # print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))
    print(find_short("turns out random test cases are easier than writing out basic ones"))


