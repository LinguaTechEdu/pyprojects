"""
Simple Calculator

Create a calculator that can add, subtract, divide, multiply and use exponents. You should be
able to import the calculator, create an instance of it and then use methods for math operations.

BONUS: Your calculator should be able to add more than 2 numbers at a time.

Usage:
>>> from simple_calculator import Calculator
>>> c = Calculator()
>>> c.add(2, 3)
=> 5
>>> c.subtract(7, 5)
=> 2
>>> c.add(1,2,3)
=> 6

Python Learning
1. Classes
2. Instances
3. Methods
4. Imports

Further Reading:
- Classes: https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes
"""


class Calculator:
    def add(self, *args):
        return sum(args)

    def subtract(self, num1, num2):
       return num1 - num2
