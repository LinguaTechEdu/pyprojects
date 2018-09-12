"""
Greeter
Duration: 15 min

Create a script that can be run from the terminal like so:
>>> python greeter.py my_name
Return => Hello, my_name!

Python Learning:
1. Module
2. sys module
3. String.format()
4. Variables

Concepts:
* Objects
* Arguments
* Printing
* Formatting
* Executing scripts

Further Reading:
- https://pymotw.com/3/sys/imports.html
- https://docs.python.org/3/library/sys.html
"""
import sys

greeting = "Hello, {}!".format(sys.argv[1])
print(greeting)
