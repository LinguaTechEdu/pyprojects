"""
File Counter

Write a script that creates several files in the current directory, searches the current directory,
lists the name of each file and returns a total count of all current files.

Each new file should be assigned a random name and have no extension.

Python Learning
1. File I/O operations using os module
2. __name__
3. try/except (error handling)
4. with
"""
import os
from name_generator import *


def create_files(count=5, suffix='.practice'):
    try:
        os.mkdir('./data')
    except FileExistsError:
        print("Directory already exists. Continuing ...")

    for _ in range(count):
        filename = generate_filename('CNTR', suffix)
        with open('./data/{}'.format(filename), 'w+') as file:
            file.write("Generic file {}".format(filename))


def list_files():
    for path, dir, file in os.walk('./data/'):
        print(file)


if __name__ == '__main__':
    create_files()
    list_files()
