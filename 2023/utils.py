import numpy as np
import math as m
import functools
import operator
import re

DIGITS = ["zero","one","two","three","four","five","six","sveven","eight","nine"]
LETTERS = [letter for letter in "abcdefghijklmnopqrstuvwxyz"]

def mul(lst):
    "like sum() but with multiplication"
    m = 1
    for el in lst:
        m*=el
    return el

def concatenate(lst):
    "concatenate a list of strings"
    return functools.reduce(operator.add,lst)

def findall(str,val):
    return [m.start() for m in re.finditer(val,str)]