"""
File Name Generator

Create a script that returns a unique file name.

Python Learning:
1. Lists
3. Arguments
"""
import random
import string
from datetime import datetime


def generate_random_string(size=26):
    letters = string.ascii_lowercase
    max_length = 26
    s = ''
    for i in range(size):
        num = random.choice(range(max_length))
        s += letters[num]

    print(s)
    return s


def generate_filename(prefix='file'):
    date = datetime.utcnow()
    stub = generate_random_string(6)
    return "{}_{}_{}".format(prefix, stub, date)
