import re
import numpy as np
import math
from math import sqrt

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


# Camel-Case
def to_camel_case(text):
    if len(text) == 0 : return "An empy string was provided but not returned"
    
    
    
    return

# Maskify
def maskify(cc):
    if len(cc) == 0: return ""
    if len(cc)<=4:
        return cc
    
    theText = ""
    
    rep = str(cc)[:len(cc) - 4]
    for i, v in enumerate(str(cc)[:len(cc) - 4]):
        theText += "#"
    
    
    return theText + str(cc)[-4:]
    

# maskify bästa !
def maskify2(cc):
    return "#"*(len(cc)-4) + cc[-4:]


def divisors(tal):
    int_arr = []
    
    for n in range(2,int(tal)):
        if int(tal) % n == 0:
            int_arr.append(n)
    
    if len(int_arr) == 0:
        return str(tal) + " is prime"
    else:
        return int_arr


def divisors_final(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l

if __name__ == '__main__':
    init()
    print(divisors(25))
    


