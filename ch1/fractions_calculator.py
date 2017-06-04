'''
Exercise 4 - Fractions calculator:
    - Write a calculator tha can perforn the basic math functions on two fractions
'''

from fractions import Fraction

def add(a,b):
    print('{0} + {1} = {2}'.format(a,b,a+b))

def subtract(a,b):
    print('{0} - {1} = {2}'.format(a,b,a-b))

def multiply(a,b):
    print('{0} x {1} = {2}'.format(a,b,a*b))

def divide(a,b):
    print('{0} / {1} = {2}'.format(a,b,a/b))

if __name__ == '__main__':
    a = Fraction(input('Enter first fraction: '))
    b = Fraction(input('Enter second fraction: '))
    op = input('Operation to perform - +, -, *, /: ')

    if op == '+':
        add(a,b)
    elif op == '-':
        subtract(a,b)
    elif op == '*':
        multiply(a,b)
    elif op == '/':
        divide(a,b)
    else:
        print('Invalid operation: {0}'.format(op))

