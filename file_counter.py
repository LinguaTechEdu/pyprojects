"""
File Counter

Write a script that creates several files in the current directory, searches the current directory,
lists the name of each file and returns a total count of all current files.

Each new file should be assigned a random name and have no extension.

Python Learning
1. File I/O operations using os module
2. __name__
3. try/except
4. with
"""
import os


def create_files(count=5):
    try:
        os.mkdir('./data')
    except FileExistsError:
        print("Directory already exists. Continuing ...")

    for i in range(count):
        with open('./data/file{}'.format(i), 'w+') as file:
            file.write("Generic file {}".format(i))


def list_files():
    for path, dir, file in os.walk('./data/'):
        print(file)


if __name__ == '__main__':
    create_files(3)
    list_files()
